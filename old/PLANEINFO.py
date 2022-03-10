from enum import Enum

# Stores the number of weapons per slot for each plane
class PlaneInfo(Enum):
    T21 = [1, 0, 0, 'T-21']
    TF4 = [0, 1, 0, 'TF-4E']
    MG21 = [4, 0, 0, 'MiG-21']
    SV37 = [4, 3, 0, 'AJS-37']
    FE4 = [3, 4, 2, 'F-4E']
    FC16 = [5, 4, 0, 'F-16C']
    CR105 = [3, 3, 4, 'CF-105']
    SK25U = [10, 10, 9, 'Su-25']
    MG31 = [3, 1, 0, 'MIG-31']
    FD14 = [4, 3, 3, 'F-14D']
    MG29 = [3, 4, 4, 'MiG-29']
    ACCIPITER = [6, 6, 5, 'AV-8']
    FE18 = [2, 9, 0, 'F-18E']
    FC15 = [3, 2, 3, 'F-15C']
    SK27 = [6, 3, 0, 'SU-27']
    SK37 = [3, 2, 0, 'SU-37']
    FS15 = [3, 2, 3, 'F-15SMTD']
    VX23 = [4, 2, 3, 'F-22']
    ACG01 = [11, 3, 5, 'ACG-01']