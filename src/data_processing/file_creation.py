import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
import xlsxwriter
import datetime
import os


def fit(times, data_matrix, fix_ends=True, make_plot=True,
        options={}, method='L-BFGS-B'):

    t = np.array(times)
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

    k = end['x'][0]

    if not fix_ends:
        a0 = end['x'][1]
        ai = end['x'][2]

    if make_plot:
        plt.figure()
        plt.plot(t, data_matrix[:, 0], 'ro')
        plt.plot(t, a0 + (ai-a0)*(1-np.exp(-k*t)))

    return (k, a0, ai)


def create_plot(lipid_name, output_dict, output_filename=None):
    times = output_dict['times']
    data_mat = output_dict['data_matrix']
    k, a0, ai = output_dict['kinetic_parameters']

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
        plt.scatter(rt, mz, label=str(
            times[all_isos.index(iso_dat)]) + " hours")
    plt.xlabel('rt')
    plt.ylabel('mz')
    plt.legend()

    if output_filename:
        plt.savefig(output_filename)
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


def create_xlsx_output(output_list, lipids, filenames, output_filename=None, auto_open=True):
    if not os.path.exists('output'):
        os.makedirs('output')

    if not output_filename:
        now = str(datetime.datetime.now()).split(' ')
        output_filename = 'output' + os.sep + now[
            0].replace('-', '_') + '_'+now[1].replace(':', '_') + '.xlsx'

    workbook = xlsxwriter.Workbook(
        output_filename, {'nan_inf_to_errors': True})
    print('Writing to {}'.format(output_filename))
    for lipid_index, lipid in enumerate(lipids):
        label = list(lipid.keys())[0].strip('\n')

        row_num = 1
        sheet_name = label.replace(':', ' ')
        sheet_name = sheet_name.replace('[', '(')
        sheet_name = sheet_name.replace(']', ')')
        worksheet = workbook.add_worksheet(sheet_name)
        cell = col2alphabet(1) + str(row_num)
        worksheet.write(cell, label)
        row_num += 1
        write_list = ['Kinetic Parameters', 'k:',
                      output_list[lipid_index]['kinetic_parameters'][0],
                      'ai:',
                      output_list[lipid_index]['kinetic_parameters'][1],
                      'a0:',
                      output_list[lipid_index]['kinetic_parameters'][2]]
        write_xlsx_block(worksheet, write_list, row_num, 1)
        row_num += 2
        write_xlsx_block(worksheet, ['isotope data'], row_num, 1)

        data_mat = output_list[lipid_index]['data_matrix']
        n_time, n_iso = data_mat.shape

        iso_list = range(n_iso)
        times = output_list[lipid_index]['times']
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
        all_isos = output_list[lipid_index]['all_isos']
        for index, iso_data in enumerate(all_isos):
            write_xlsx_block(worksheet, filenames[index], row_num, 2)
            row_num += 1
            for row in iso_data:
                write_xlsx_block(worksheet, row, row_num, 3)
                row_num += 1

        create_plot(
            label, output_list[lipid_index],
            output_filename='temp_{}.png'.format(label))
        worksheet.insert_image('N4', 'temp_{}.png'.format(label))
    workbook.close()
    print('\nComplete!')
    print('Output File at: ' +
          os.getcwd() + os.sep + output_filename)
    if auto_open:
        os.system(os.getcwd() + os.sep + output_filename)


def min_func(x, *args):
    p = args
    k = x[0]
    t = p[1]
    data = p[2]

    if p[0]:
        a0 = p[3]
        ai = p[4]
    else:
        a0 = x[1]
        ai = x[2]
    preds = a0 + (ai-a0)*(1-np.exp(-k*t))

    return ((preds-data)**2).sum()
