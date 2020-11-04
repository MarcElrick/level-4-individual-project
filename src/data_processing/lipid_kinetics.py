import numpy as np
from mass_spec_utils.data_import.mzml import MZMLFile
from mass_spec_utils.adduct_calculator.adduct_rules import AdductTransformer


def compute_lipid_kinetics(lipid_details, files):
    data_matrix = np.zeros((len(files), lipid_details['isotopeDepth'] + 1))

    for (filename, time) in files:
        pass
        # DO MORE STUFF HERE


def get_isotope_intensity(lipid_details, file, scan_delta=2):
    file[0] = MZMLFile(file[0])

    scans_in_range = list(filter(lambda x: x.rt_in_seconds >= lipid_details['retentionTime'] - lipid_details['retentionTimeTolerance'] and
                                 x.rt_in_seconds <= lipid_details['retentionTime'] + lipid_details['retentionTimeTolerance'], file[0].scans))

    spectrum = lipid_details['formula'].spectrum()
    print(spectrum)

    # _______________________________________
    # THIS TAKES A LONG TIME - POSSIBLE OPTIMISATION
    target_mass = [AdductTransformer().mass2ion(x[0], lipid_details['adduct'])
                   for x in spectrum.values()]

    target_mass.sort()
    current_mass = target_mass[0]
    # _______________________________________
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
        intensity, exact_mass = get_max_mass(scan, current_mass - absolute_mass_tolerance,
                                             current_mass + absolute_mass_tolerance)
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
