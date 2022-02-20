import sys
import random
import PLANEINFO
# Stores all weapons available in the game
weaponsMaster = ['stdm', 'stdm2', 'mlaa', 'mlaa2', 'mlaa3', 'saa', 'mlag', 'mlag2', 'adm', 'ugbs', 'ugbs3', 'ugbl',
                 'bdu16', 'gbs', 'gbs3', 'urs', 'urmb', 'urm', 'droptank', 'rgp', 'mgp', 'hgp', 'rgps', 'sr', 'sr2',
                 'cgp', 'hvsm', 'hism', 'asm']

# Non working and removed weapons
# 'hmaa', 'rdbm', 'eubm', 'eufb', 'bmlaa', 'rgpi', 'mgpi', 'hgpi', 'cgpi', 'rg', 'cbl'

seed = sys.argv[1]

random.seed(seed)
r = random.Random(seed)

numWeps = len(weaponsMaster)

# Shuffle the main weapons list
random.shuffle(weaponsMaster)

dtp = open(r".\ProjectWingman\sicario\pw-randomizer.dtp", "a")


# Iterate over all the planes
for PLANE in PLANEINFO.PlaneInfo:
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

dtp.close()