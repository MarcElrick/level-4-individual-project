# A collection of single purpose, general functions that are used in multiple places
import os


def mass2iso(mono_iso_mass, mass_multi, mass_add):
    return mono_iso_mass * mass_multi + mass_add


def getFilenameFromPath(filepath):
    if filepath == "":
        return ""
    return os.path.abspath(filepath).split(os.sep)[-1]


def parse_adduct_file(file):
    with open(file) as f:
        adduct_list = [line.strip('\n').split(',') for line in f][1:]
        for adduct in adduct_list:
            adduct[1] = float(adduct[1])
            adduct[2] = float(adduct[2])
        return adduct_list
