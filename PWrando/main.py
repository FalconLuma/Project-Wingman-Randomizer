import sys
import random
from enum import Enum

# Stores all weapons available in the game
weaponsMaster = ['stdm', 'stdm2', 'mlaa', 'mlaa2', 'mlaa3', 'saa', 'mlag', 'mlag2', 'adm', 'ugbs', 'ugbs3', 'ugbl',
                 'bdu16', 'gbs', 'gbs3', 'urs', 'urmb', 'urm', 'droptank', 'rgp', 'mgp', 'hgp', 'rgps', 'sr', 'sr2',
                 'cgp', 'hvsm', 'hism', 'asm']

# Non working and removed weapons
# 'hmaa', 'rdbm', 'eubm', 'eufb', 'bmlaa', 'rgpi', 'mgpi', 'hgpi', 'cgpi', 'rg', 'cbl'

# Stores the number of weapons per slot for each plane
class PlaneSlots(Enum):
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


print('Welcome to the Project Wingman Randomizer')
print('Please enter a seed or press enter to use a random seed')

# Read in the seed and remove the newline char
for line in sys.stdin:
    seed = line.strip('\n')
    break

# If no seed was entered create a random one
if seed == '':
    seed = int(random.randrange(sys.maxsize))

random.seed(seed)
r = random.Random(seed)

# Print the seed back to the user
print('Your seed is: ' + str(seed))

numWeps = len(weaponsMaster)

# Shuffle the main weapons list
random.shuffle(weaponsMaster)

dtp = open(r".\ProjectWingman\sicario\pw-randomizer.dtp", "w+")
dtpStart = ["{\n", ' "meta": {\n', '  "DisplayName": "Randomizer: ' + str(seed) + '",\n', '  "Author": "FalconLuma"\n',
            ' },\n',
            ' "modParameters": {},\n', ' "mods": [{\n', '  "FilePatches": {},\n', '  "AssetPatches": {\n',
            '   "ProjectWingman/Content/ProjectWingman/Blueprints/Data/AircraftData/DB_Aircraft.uexp": [\n']
dtp.writelines(dtpStart)

# Iterate over all the planes
for PLANE in PlaneSlots:
    dtp.write('    {\n     "name": "' + PLANE.name + ' Random Loadout",\n     "patches": [\n      {\n       '
              '"description": "Calibrate HardpointCompatibilityList",\n       "template": "datatable:[' + "'" +
              PLANE.value[3] + "'" + '''].[0].{'HardpointCompatibilityList*'}",\n''''       "value": "StrProperty:[' + "'" + 'stdm')
    # print(PLANE.name)
    s = 0
    # Iterate over all 3 of each plane's slots
    while s < 3:
        weapons = weaponsMaster.copy()
        a = PLANE.value[s]
        w = [0 for _ in range(a)]
        i = 0
        while i < a:
            # When no weapon is selected '' re-roll
            # when a weapon is chosen remove it from the pool for this slot to avoid duplicates in the same slot
            weapon = ''
            while weapon == '':
                wepNum = random.randint(0, numWeps - 1)
                weapon = weapons[wepNum]
            w[i] = weapon
            weapons[wepNum] = ''
            i = i + 1
        if PLANE.value[3] == 'TF-4E' and s == 0:
            dtp.write("','0")
        if a != 0:
            dtp.write("','0")
            for sw in w:
                dtp.write("," + str(sw))

        s = s + 1
    dtp.write("']" + '",\n       "type": "arrayPropertyValue"\n')
    dtp.write('      }\n     ]\n    },\n')

dtpEnd = ['   ]\n', '  }\n', ' }]\n', '}']
dtp.writelines(dtpEnd)
dtp.close()
