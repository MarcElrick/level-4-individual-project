import numpy as np
import matplotlib.pyplot as plt

from mass_spec_utils.data_import.mzml import MZMLFile
from mass_spec_utils.adduct_calculator.adduct_rules import AdductTransformer
from scipy.optimize import minimize


def compute_lipid_kinetics(lipid_details, files):
    data_matrix = np.zeros((len(files), lipid_details['isotopeDepth'] + 1))

    discard_index = -1
    all_isos = []

    for index, (filepath, time) in enumerate(files):
        isotopes = get_isotope_intensity(lipid_details, [filepath, time])

        if index == 0:
            # check that intensities are monotonically decreasig. If not, chop.
            for (i, _, intensity, _, _, _) in isotopes[:-1]:
                if intensity < isotopes[i+1][2]:
                    discard_index = i
                    break
        for (i, _, intensity, _, _, _) in isotopes:
            if discard_index > -1 and i > discard_index:
                data_matrix[index, i] = 0
            else:
                data_matrix[index, i] = intensity

        all_isos.append(isotopes)
    if discard_index > -1:
        data_matrix = data_matrix[:, :discard_index+1]

    times = [t for (f, t) in files]

    data_matrix /= data_matrix.sum(axis=1)[:, None]
    p = fit(times, data_matrix, fix_ends=False, make_plot=False)
    k, a0, ai = p

    output_dict = {}
    output_dict['kinetic_parameters'] = (k, a0, ai)
    output_dict['data_matrix'] = data_matrix
    output_dict['times'] = times
    output_dict['all_isos'] = all_isos

    return output_dict


def get_isotope_intensity(lipid_details, filepair, scan_delta=2):
    filepair[0] = MZMLFile(filepair[0])

    scans_in_range = list(filter(lambda x: x.rt_in_seconds >=
                                 lipid_details['retentionTime'] -
                                 lipid_details['retentionTimeTolerance'] and
                                 x.rt_in_seconds <=
                                 lipid_details['retentionTime'] +
                                 lipid_details['retentionTimeTolerance'],
                                 filepair[0].scans))

    spectrum = lipid_details['formula'].spectrum()

    myTransformer = AdductTransformer()

    target_mass = [myTransformer.mass2ion(x[0], lipid_details['adduct'])
                   for x in spectrum.values()]

    target_mass.sort()
    current_mass = target_mass[0]

    isotopes = []
    # Is this an error? why would we calculate the tolerance using only the first value of target mass?
    if lipid_details['massToleranceUnits'] == 'ppm':
        absolute_mass_tolerance = ppm_to_da(
            current_mass, lipid_details['massTolerance'])
    else:
        absolute_mass_tolerance = lipid_details['massTolerance']

    max_intensity = 0
    max_intensity_index = 0
    max_mass = 0
    max_retention_time = 0
    max_scan_no = 0

    for scan in scans_in_range:
        intensity, exact_mass = get_max_mass(scan, current_mass -
                                             absolute_mass_tolerance,
                                             current_mass
                                             + absolute_mass_tolerance)
        if intensity >= max_intensity:
            max_intensity = intensity
            max_intensity_index = scans_in_range.index(scan)
            max_mass = exact_mass
            max_retention_time = scan.rt_in_seconds
            max_scan_no = scan.scan_no
    isotopes.append((0, current_mass, max_intensity, max_mass,
                     max_retention_time, max_scan_no))

    pos = 0
    for current_mass in target_mass[1:]:
        pos += 1
        if pos > lipid_details['isotopeDepth']:
            break
        max_intensity = 0
        max_mass = -1
        max_retention_time = None
        max_scan_no = None

        for scan_index in range(max_intensity_index-scan_delta, max_intensity_index+scan_delta+1):
            if scan_index >= 0 and scan_index < len(scans_in_range):
                scan = scans_in_range[scan_index]
                intensity, exact_mass = get_max_mass(
                    scan, current_mass - absolute_mass_tolerance, current_mass + absolute_mass_tolerance)
                if intensity >= max_intensity:
                    max_intensity = intensity
                    max_mass = exact_mass
                    max_retention_time = scan.rt_in_seconds
                    max_scan_no = scan.scan_no
        isotopes.append((pos, current_mass, max_intensity,
                         max_mass, max_retention_time, max_scan_no))
    return isotopes


def ppm_to_da(mass, tolerance):
    return mass * tolerance / 1e6


# Taken directly from prototype - need to test.
def get_max_mass(scan, mz_min, mz_max):
    sub_peaks = list(
        filter(lambda x: x[0] >= mz_min and x[0] <= mz_max, scan.peaks))
    if len(sub_peaks) == 0:
        return 0.0, -1
    else:
        mz, intensity = zip(*sub_peaks)
        max_i = max(intensity)
        max_mz = np.array(mz)[np.argmax(intensity)]
        return max_i, max_mz


def fit(times, data_matrix, fix_ends=True, make_plot=True, options={}, method='L-BFGS-B'):

    t = np.array(times)
    print('times', times)
    a0 = data_matrix[0, 0]
    ai = data_matrix[-1, 0]

    k = 0.05

    if fix_ends:
        args = (fix_ends, t, data_matrix[:, 0], a0, ai)
        zinit = [k]
    else:
        args = (fix_ends, t, data_matrix[:, 0])
        zinit = [k, a0, ai]

    end = minimize(min_func, zinit, args=args, method=method)

    if fix_ends:
        k = end['x'][0]
    else:
        a0 = end['x'][1]
        ai = end['x'][2]

    if make_plot:
        plt.figure()
        plt.plot(t, data_matrix[:, 0], 'ro')
        plt.plot(t, a0 + (ai-a0)*(1-np.exp(-k*t)))

    return (k, a0, ai)


def min_func(x, *args):
    # x = k: the rate constant
    # *args

    p = args
    if p[0] == True:
        t = p[1]
        data = p[2]
        a0 = p[3]
        ai = p[4]

        k = x[0]
    else:
        t = p[1]
        data = p[2]

        k = x[0]
        a0 = x[1]
        ai = x[2]
    preds = a0 + (ai-a0)*(1-np.exp(-k*t))

    return ((preds-data)**2).sum()


def create_plot(lipid_name, output_dict, output_filename=None):
    times = output_dict['times']
    data_mat = output_dict['data_matrix']
    k, a0, ai = output_dict['kinetic_parameters']

    print("OUTPUT", output_dict['times'])

    plt.figure(figsize=(20, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(data_mat, aspect='auto')
    plt.xlabel('isotope')
    plt.ylabel('time')
    plt.yticks(range(len(times)), times)
    plt.title(lipid_name)

    plt.colorbar()
    plt.subplot(1, 3, 2)
    t = np.array(times)
    plt.plot(t, data_mat[:, 0], 'ro')
    plt.plot(t, a0 + (ai-a0)*(1-np.exp(-k*t)))
    plt.title('{}  k: {:.3f}, a0: {:.3f}, ai: {:.3f}'.format(
        lipid_name, k, a0, ai))

    plt_name = '{}_condition_{}_{}.png'.format(
        '_'.join(lipid_name.split()), 1, 'Pos').replace(':', '_')

    all_isos = output_dict['all_isos']
    plt.subplot(1, 3, 3)

    for iso_dat in all_isos:
        mz = []
        rt = []
        for iso in iso_dat:
            iso_mz = iso[3]
            iso_rt = iso[4]
            if iso_mz > 0:  # it's -1 if not found
                mz.append(iso_mz)
                rt.append(iso_rt)
       # plt.scatter(rt, mz, label="{:5.5s}".format(f.split(os.sep)[-1]))
        plt.scatter(rt, mz, label=str(
            times[all_isos.index(iso_dat)]) + " hours")
    plt.xlabel('rt')
    plt.ylabel('mz')
    plt.legend()

    if output_filename:
        #         plt.savefig(os.path.join('plots',plt_name))
        #         print("Writing: ",plt_name)
        plt.savefig(output_filename)
        print("Writing: ", output_filename)
    plt.close()


def col2alphabet(col_num):
    prefix = (col_num // 26)
    nextfix = col_num % 26
    if prefix == 0:
        alppre = ''
    else:
        alppre = chr(prefix + 65 - 1)
    alp = chr(nextfix + 65)
    return alppre + alp


def write_xlsx_block(worksheet, list_vals, row_num, start_col):
    for i, v in enumerate(list_vals):
        cell = col2alphabet(start_col+i) + str(row_num)
        worksheet.write(cell, v)


def create_xlsx_output(output_dict, output_filename='test.xlsx'):
    workbook = xlsxwriter.Workbook(
        output_filename, {'nan_inf_to_errors': True})
    for lipid_no, lipid in enumerate(output_dict):
        row_num = 1
        sheet_name = lipid.replace(':', ' ')
        sheet_name = sheet_name.replace('[', '(')
        sheet_name = sheet_name.replace(']', ')')
        worksheet = workbook.add_worksheet(sheet_name)
        cell = col2alphabet(1) + str(row_num)
        worksheet.write(cell, lipid)
        row_num += 1
        write_list = ['Kinetic Parameters', 'k:',
                      output_dict[lipid]['kinetic_parameters'][0],
                      'ai:',
                      output_dict[lipid]['kinetic_parameters'][1],
                      'a0:',
                      output_dict[lipid]['kinetic_parameters'][2]]
        write_xlsx_block(worksheet, write_list, row_num, 1)
        row_num += 2
        write_xlsx_block(worksheet, ['isotope data'], row_num, 1)

        data_mat = output_dict[lipid]['data_mat']
        n_time, n_iso = data_mat.shape

        iso_list = range(n_iso)
        times = output_dict[lipid]['times']
        write_xlsx_block(worksheet, iso_list, row_num, 3)
        row_num += 1
        for i, row in enumerate(data_mat):
            dlist = [times[i]] + list(row)
            write_xlsx_block(worksheet, dlist, row_num, 2)
            row_num += 1

        row_num += 1
        write_xlsx_block(worksheet, ['isotope details', 'file', 'iso number',
                                     'theoretical m/z', 'intensity', 'mz', 'rt', 'scan number'], row_num, 1)
        row_num += 1
        all_isos = output_dict[lipid]['all_isos']
        for filename, iso_data in all_isos.items():
            write_xlsx_block(worksheet, [filename], row_num, 2)
            row_num += 1
            for row in iso_data:
                write_xlsx_block(worksheet, row, row_num, 3)
                row_num += 1

        create_plot(
            lipid, output_dict[lipid], output_filename='temp_{}.png'.format(lipid_no))
        worksheet.insert_image('N4', 'temp_{}.png'.format(lipid_no))
    workbook.close()

    for lipid_no, lipid in enumerate(output_dict):
        os.system('rm temp_{}.png'.format(lipid_no))
