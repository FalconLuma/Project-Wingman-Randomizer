import sys
import random
from enum import Enum

# Stores all weapons available in the game
weaponsMaster = ['stdm', 'stdm2', 'mlaa', 'mlaa2', 'mlaa3', 'saa', 'hmaa', 'mlag', 'mlag2', 'adm', 'ugbs', 'ugbs3',
                 'ugbl', 'bdu16', 'gbs', 'gbs3', 'urs', 'urmb', 'urm', 'droptank', 'rgp', 'mgp', 'hgp', 'rg', 'rgps',
                 'rdbm', 'eubm', 'eufb', 'bmlaa', 'sr', 'sr2', 'cgp', 'hvsm', 'cbl', 'hism', 'asm', 'rgpi', 'mgpi',
                 'hgpi', 'cgpi']


# Stores the number of weapons per slot for each plane
class PlaneSlots(Enum):
    T21 = [1, 0, 0]
    TF4 = [0, 1, 0]
    MG21 = [4,0,0]
    SV37 = [4,3,0]
    FE4 = [3,4,2]
    FC16 = [5,4,0]
    CR105 = [3,3,4]
    SK25U = [10,10,9]
    MG31 = [3,1,0]
    FD14 = [4,3,3]
    MG29 = [3,4,4]
    ACCIPITER = [6,6,5]
    FE18 = [2,9,0]
    FC15 = [3,2,3]
    SK27 = [6,3,0]
    SK37 = [3,2,0]
    FS15 = [3, 2, 3]
    VX23 = [4,2,3]
    ACG01 = [11,3,5]


print('Welcome to the Project Wingman Randomizer')
print('Please enter a seed or press enter to use a random seed')

# Read in the seed and remove the newline char
for line in sys.stdin:
    seed = line.strip('\n')
    break

# If no seed was entered create a random one
if seed == '':
    seed = random.randrange(sys.maxsize)

random.seed(seed)
r = random.Random(seed)

# Print the seed back to the user
print('Your seed is: ' + str(seed))

numWeps = len(weaponsMaster)

# Shuffle the main weapons list
random.shuffle(weaponsMaster)

# Iterate over all the planes
for PLANE in PlaneSlots:
    print(PLANE.name)
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
        print(w)
        s = s + 1
