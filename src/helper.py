# A collection of single purpose, general functions that are used in multiple places
import os


def getFilenameFromPath(filepath):
    if filepath == "":
        return ""
    return os.path.abspath(filepath).split(os.sep)[-1]
