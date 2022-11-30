# -*- coding: utf-8 -*-

"""
@author: FalconLuma

Randomizer project for Project Wingman
"""

import random
import sys
import tkinter as tk
from tkinter import ttk
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
    SPEAR = [1, 1, 1, 'SPEAR']
    PWMK1 = [1, 1, 0, 'PW-001']
    CR105C = [5,6,5, 'CF-105_2']
    MG21C = [3,0,0, 'MiG-21_2']
    ACCIPTERC = [6,6,6,'AV-8_2']



print("Launching Randomizer")

#Window declared here
window = tk.Tk()

WEAPONSNAMES = [['MSSL', 'stdm', 'STDM'], ['MSSL_Multi2', 'stdm2', 'STDM-2'], ['HVSM', 'hvsm', 'HVSM'], ['HISM', 'hism', 'HISM'], ['RDBM', 'rdbm', 'RDBM'], ['BMLAA', 'bmlaa', 'BML-U'],
                ['XMA4', 'mlaa', 'MLAA'], ['XMA4_Multi2', 'mlaa2', 'MLAA-2'], ['XMA4_Multi3', 'mlaa3', 'MLAA-3'], ['SAAM', 'saa', 'SAA'],
                ['ASM', 'asm', 'ASM'], ['AGM', 'mlag', 'MLAG'], ['AGM_Multi2', 'mlag2', 'MLAG-2'], ['GBS', 'gbs', 'GBS'], ['GBS_Multi3', 'gbs3', 'GBS-3'],
                ['UGBS', 'ugbs', 'UGBS'], ['UGBS_Multi3', 'ugbs3', 'UGBS-3'], ['UGBL', 'ugbl', 'UGBL'], ['DropTank', 'droptank', 'DT'], ['EUFB', 'eufb', 'EUFB'], ['BDU16', 'bdu16', 'BDU-16'],
                ['URS', 'urs', 'URS'], ['URM', 'urm', 'URM'], ['URMB', 'urmb', 'URMB'], ['SR', 'sr', 'SR'], ['SR-2', 'sr2', 'SR-2'],
                ['Gunpod_LITE', 'rgp', 'RGP'], ['Gunpod_MID', 'mgp', 'MGP'], ['Gunpod_HVY', 'hgp', 'HGP'], ['Gunpod_CAN', 'cgp', 'CGP'], ['RailgunGunpod', 'rgpd', 'RG']]

WEAPONSMASTER = ['stdm', 'stdm2', 'hvsm', 'hism', 'rdbm', 'bmlaa',
                 'mlaa', 'mlaa2', 'mlaa3', 'saa',
                 'asm', 'mlag', 'mlag2', 'gbs', 'gbs3',
                 'ugbs', 'ugbs3', 'ugbl', 'droptank', 'eufb', 'bdu16',
                  'urs', 'urm', 'urmb', 'sr', 'sr2', 'rgp', 'mgp', 'hgp', 'cgp','rgpd']

weaponsNames = []
weaponsMaster = []

weaponsSelected = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True]

# Plane Stat Ranges [Min, Max] Tuples
pStatNames = ['Response', 'Speed', 'Accel', 'Roll', 'Turn', 'Yaw']
pStatRanges = [[1.0, 7.0], [1000, 4000], [25, 200], [50, 350], [50, 300], [5, 30]] # Response, Speed, Accel, Roll, Turn, Yaw

# Weapon Stat Ranges [Min, Max] Tuples
wStatNames = ['Reload', 'Ammunition', 'Loaded', 'Max Locks', 'Range', 'Gun Reload', 'Gun Ammo']
wStatRanges = [[3, 40], [8, 182], [1, 20], [1, 44], [2800, 12000], [0.01, 0.2], [320, 3800]] # Reload, Ammo, Proj, Salvo, Range, GunReload, GunAmmo

unguidedChance = 0.5

attrs = ['InterpSpeed', 'MaxSpeed', 'Acceleration', 'RollSpeed', 'TurnSpeed', 'YawSpeed']

npcAicraft = ['AJS-37', 'F-18E', 'F-18F', 'F-18EADV', 'SU-27', 'MIG-31', 'F-15C', 'F-14D', 'F-22', 'F-16C', 'C-17',
              'C-17_Fast', 'C-17_Faster', 'B-52', 'AS-02', 'DV-204', 'FC-8', 'SU-37', 'F-15SMTD', 'SU-30', 'F-4E',
              'PW-01', 'J-10B', 'SU-25', 'Spear', 'CruiseMissile', 'CruiseMissile_Buff', 'CF-8', 'QGMk3', 'BCS4',
              'MIG-29', 'MIG-21', 'AV-8', 'CHIMERA', 'CIV-8']
naStatNames = ['BaseHP', 'RollSpeed', 'TurnSpeed', 'YawSpeed', 'DefaultSpeed', 'Acceleration']
naStatRanges = [[10, 400], [15, 300], [5, 200], [5, 200], [400, 1000], [100, 600]]

OpSlotRanges = [1, 11]

missionNames = ['C02_Frontiers', 'C03_Homestead', 'C04_Uphill', 'C05_Sirens', 'C06_MachineOfTheMantle',
                'C07_EminentDomain', 'C08_ClearSkies', 'C09_SteppingStone', 'C10_PillarsOfComm', 'C11_ColdWar',
                'C13_MidnightLight', 'C14_Valkyrie', 'C15_OpenSeason', 'C16_ConsequenceOf', 'C16B_Unfortunate',
                'C17_NoRespite', 'C18_Return', 'C19_RedSea', 'C20_Presidia', 'C22_Kings']

missionIDList = ['campaign_02','campaign_03','campaign_04','campaign_05','campaign_06','campaign_07','campaign_08',
                 'campaign_09', 'campaign_10','campaign_11','campaign_13','campaign_14', 'campaign_15','campaign_16',
                 'campaign_16.2','campaign_17','campaign_18','campaign_19','campaign_20','campaign_22']

missionPointers = dict()
for i, m in enumerate(missionIDList):
    if i < len(missionIDList) - 1:
        missionPointers[m] = missionIDList[i + 1]
    else:
        missionPointers[m] = 'ending'

print(missionPointers)
filepath = r"./ProjectWingman/Content/Paks/~mods/pw-randomizer.dtp"

rLoad = tk.BooleanVar()
rStats = tk.BooleanVar()
rWeps = tk.BooleanVar()
rOpSlot = tk.BooleanVar()
# Generates a random seed

def genSeed():
    t1.delete('1.0', 'end')
    seed = int(random.randrange(sys.maxsize))
    global seedGens
    seedGens = seedGens + 1
    t1.insert('end', str(seed))
    # Only allows one seed to be randomized
    b1.config(state='disabled')

# Manages running the randomizer
def runRando():
    print('Starting Randomizer')
    seed = t1.get('1.0', 'end').strip('\n')
    try:
        variants = int(t2.get('1.0', 'end').strip('\n'))
    except:
        variants = 1
    global seedGens

    if seedGens == 0:
        # If the seed wasn't randomized runs a single rng to allow for random seeds to be repeatable
        random.randrange(sys.maxsize)

    #Prepare weapons lists
    i = 0
    while i < len(WEAPONSMASTER):
        if weaponsSelected[i]:
            weaponsNames.append(WEAPONSNAMES[i])
            weaponsMaster.append(WEAPONSMASTER[i])
        i = i + 1

    # Try to open/create the dtp, at minimum the ~mods folder must exist, otherwise display an error message
    try:
        dtp = open(filepath, "w+")
    except:
        labelError.pack()
    # Clear the DTP file of all text before starting
    dtp.truncate(0)
    dtpStart = ["{\n",
                '    "modParameters": {},\n',
                '    "mods": [{\n',
                '        "_meta": {\n',
                '            "DisplayName": "Project Wingman Randomizer: ' + str(seed) + '",\n',
                '            "Author": "FalconLuma"\n',
                '        },\n',
                '        "FilePatches": {},\n',
                '        "AssetPatches": {\n']
    dtp.writelines(dtpStart)
    dtp.close()

    #npcAirRando(seed)
    missionOrderRando(seed)

    dtp = open(filepath, "a")


    # Unlock normally unavailable weapons
    unlockText = ['            "ProjectWingman/Content/ProjectWingman/Blueprints/Data/Weapons/DWeaponDB.uexp": [\n',
                  '                {',
                  '                    "name": "Make all weapons available",\n',
                  '                    "patches": [\n',
                  '                        {\n',
                  '                            "description": "Make all weapons available",\n',
                  '''                            "template": "datatable:{'IsAvailable*'}",\n'''
                  '                            "value": "BoolProperty:true",\n',
                  '                            "type": "propertyValue"\n',
                  '                        },\n',
                  '                        {\n',
                  '                            "description": "Make al weapons available outside Conquest",\n',
                  '''                            "template": "datatable:{'CQOnly*'}",\n''',
                  '                            "value": "BoolProperty:false",\n',
                  '                            "type": "propertyValue"\n',
                  '                        }\n',
                  '                    ]\n',
                  '                }\n',
                  ]
    dtp.writelines(unlockText)

    if rWeps.get():
        print('Randomizing Weapon Stats')
        dtp.writelines([',\n'])
        dtp.close()
        weaponRando(seed, variants)

    dtp = open(filepath, "a")
    wepCloseText = ['            ],\n',
                    '            "ProjectWingman/Content/ProjectWingman/Blueprints/Data/AircraftData/DB_Aircraft.uexp": [\n']
    dtp.writelines(wepCloseText)
    dtp.close()


    if rLoad.get():
        print('Randomizing Loadouts')
        loadoutRando(seed)

    if rStats.get():
        print('Randomizing Aircraft Performance')
        if rLoad.get():
            dtp = open(filepath, "a")
            dtp.writelines([',\n'])
            dtp.close()
        statRando(seed)

    dtp = open(filepath, "a")
    dtpEnd = ['            ]\n',
              '        }\n',
              '    }]\n',
              '}']
    dtp.writelines(dtpEnd)
    dtp.close()
    print('Finished Randomizing')
    print('Depending on your settings Project Sicario Merger may take more than a minute to run')
    # Display a message when the randomizer is finished

    labelFinished.pack()
    labelError.destroy()
    b2.config(state='disabled')


def loadoutRando(seed):
    random.seed(seed)
    r = random.Random(seed)

    numWeps = len(weaponsMaster)

    # Shuffle the main weapons list
    random.shuffle(weaponsMaster)

    dtp = open(filepath, "a")

    # unlock fixed weapons (SPEAR and PWMK1)
    unfixText = ['                {\n',
                 '                    "name": "un-fix loadouts",\n',
                 '                    "patches": [\n',
                 '                        {\n',
                 '                            "description": "Disable Fixed Loadouts",\n',
                 '''                            "template": "datatable:{'FixedLoadout*'}",\n''',
                 '                            "value": "BoolProperty:false",\n',
                 '                            "type": "propertyValue"\n',
                 '                        }\n',
                 '                    ]\n',
                 '                },\n'
                 ]
    dtp.writelines(unfixText)

    # Iterate over all the planes
    for PLANE in PlaneInfo:
        modTextTop = ['                {\n',
                      '                    "name": "' + PLANE.name + ' Random Loadout",\n',
                      '                    "patches": [\n',
                      '                        {\n',
                      '                            "description": "Calibrate HardpointCompatibilityList",\n',
                      '                            "template": "datatable:[' + "'" + PLANE.value[3] + "'" + '''].[0].{'HardpointCompatibilityList*'}",\n''''',
                      '                            "value": "StrProperty:[' + "'" + 'stdm'
                      ]
        dtp.writelines(modTextTop)
        s = 0
        # Iterate over all 3 of each plane's slots
        while s < 3:
            weapons = weaponsMaster.copy()
            if(rOpSlot.get()):
                if PLANE.value[s] == 0:
                    a = 0
                else:
                    a = random.randint(OpSlotRanges[0],OpSlotRanges[1])
            else:
                a = PLANE.value[s]
            w = [0 for _ in range(a)]
            i = 0
            while i < a and i < len(weaponsMaster):
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
        dtp.write("']" + '",\n                            "type": "arrayPropertyValue"\n')
        dtp.write('                        },\n')

        gunRandoText = ['                        {\n',
                        '                            "description": "Calibrate CannonType",\n',
                        '                            "template": "datatable:[' + "'" + PLANE.value[3] + "'" + '].[0].{' + "'" + 'BaseStats*' + "'" + '}.{' + "'" + 'CannonType*' + "'" + '}.<S_CannonType::>",\n',
                        '                            "value": "ByteProperty:' + "'" + 'S_CannonType::NewEnumerator' + str(random.randint(0, 2)) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        }\n'
                        ]
        dtp.writelines(gunRandoText)

        dtp.write('                    ]\n                }')
        if PLANE.value[3] != 'AV-8_2':
            dtp.write(',\n')

    dtp.close()


def statRando(seed):
    random.seed(seed)
    r = random.Random(seed)

    dtp = open(filepath, "a")

    # Iterate over all the planes
    for PLANE in PlaneInfo:
        response = round(random.uniform(pStatRanges[0][0],pStatRanges[0][1]), 1)
        speed = random.randint(pStatRanges[1][0],pStatRanges[1][1])
        accel = random.randint(pStatRanges[2][0],pStatRanges[2][1])
        roll = random.randint(pStatRanges[3][0],pStatRanges[3][1])
        turn = random.randint(pStatRanges[4][0],pStatRanges[4][1])
        yaw = random.randint(pStatRanges[5][0],pStatRanges[5][1])

        vals = [response, speed, accel, roll, turn, yaw]

        modTextTop = ['                {\n',
                      '                    "name": "' + PLANE.name + ' Random Stats",\n',
                      '                    "patches": [\n',
                      ]
        dtp.writelines(modTextTop)
        i = 0
        while i < 6:
            modText = [
                '                        {\n',
                '                            ''"description": "Modify ' + attrs[i] + '",\n',
                '                            "template": "datatable:[' + "'" + PLANE.value[3] + "'].[0].{'BaseStats*'}.{'" + attrs[i] + "*'}.<FloatProperty>" + '",\n'
                '                            ''"value": "FloatProperty:' + str(vals[i]) + '",\n',
                '                            "type": "propertyValue"\n',
                '                        }'
            ]
            dtp.writelines(modText)
            if i != 5:
                dtp.write(",\n")
            i = i + 1
        dtp.write('\n                    ]\n                }')
        if PLANE.value[3] != 'AV-8_2':
            dtp.write(',')
        dtp.write('\n')
    dtp.close()


def weaponRando(seed, variants):
    dtp = open(filepath, "a")
    weaponsMaster.clear()
    random.seed(seed)
    for w in weaponsNames:
        var = range(variants)
        for n in var:
            id = w[0] + '_' + str(n + 1)
            name = w[1] + '_' + str(n + 1)
            weaponsMaster.append(name)
            # Reload, Ammo, Proj, Salvo, Range, GunReload, GunAmmo
            stats = []  # Reload,Ammo,Proj,Salvo,Range
            i = 0
            while i < 5:
                if i == 0:
                    if w[1] in ['rgp', 'mgp', 'hgp', 'cgp']:
                        v = round(random.uniform(wStatRanges[5][0], wStatRanges[5][1]), 4)
                    else:
                        v = float(random.randint(wStatRanges[0][0], wStatRanges[0][1]))
                elif i == 1:
                    if w[1] in ['rgp', 'mgp', 'hgp', 'cgp']:
                        v = random.randint(wStatRanges[6][0], wStatRanges[6][1])
                    else:
                        v = random.randint(wStatRanges[1][0], wStatRanges[1][1])
                elif i == 2:
                    if w[1] in ['rgp', 'mgp', 'hgp', 'cgp']:
                        v = 20
                    else:
                        v = random.randint(wStatRanges[2][0], wStatRanges[2][1])
                elif i == 3:
                    if w[1] == 'rdbm':
                        v = 1
                    else:
                        v = random.randint(wStatRanges[3][0], wStatRanges[3][1])
                else:
                    if w[1] in ['rgp', 'mgp', 'hgp', 'cgp', 'rgpd']:
                        v = 0
                    else:
                        v = float(random.randint(wStatRanges[4][0], wStatRanges[4][1]))
                    # Give unguided weapons a chance to be unguided
                    if w[1] in ['ugbl', 'ugbs', 'ugbs3', 'droptank', 'eufb', 'bdu16', 'urs', 'urm', 'urmb', 'sr', 'sr2']:
                        c = round(random.uniform(0,1),2)
                        if unguidedChance >= c:
                            v = 0
                stats.append(v)
                i = i + 1

            statString = 'Reload: ' + str(stats[0]) + ',    ' + 'Ammo: ' + str(
                stats[1]) + ',    ' + 'Projectiles: ' + str(stats[2]) + ',    ' + 'Salvo: ' + str(
                stats[3]) + ',    ' + 'Range: ' + str(stats[4])

            uiName = w[2] + ' mk.' + str(n + 1)

            cloneText = ['                {\n',
                         '                    "name": "Add new weapon",\n',
                         '                    "patches": [\n',
                         '                        {\n',
                         '                            "description": "Clone ' + w[0] + '",\n',
                         '                            "template": "datatable:[*]",\n'
                         '                            "value": "' + "'" + w[0] + "'>'" + id + "'" + '",\n',
                         '                            "type": "duplicateEntry"\n',
                         '                        }\n',
                         '                    ]\n',
                         '                },\n',
                         ]
            dtp.writelines(cloneText)
            statText = ['                {\n',
                        '                    "name": "Set Stats",\n',
                        '                    "patches": [\n',
                        '                        {\n',
                        '                            "description": "Change ID",\n',
                        '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'ID*' + "'" + '}.<StrProperty>",\n'
                        '                            "value": "StrProperty:' + "'" + name + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        },\n',
                        '                        {\n',
                        '                            "description": "Change LongDesc",\n',
                        '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'WeaponLongDescription*' + "'" + '}.<TextProperty>",\n'
                        '                            "value": "' + "'" + id + "_WeaponLongDescription':'" + statString + "'" + '",\n',
                        '                            "type": "textProperty"\n',
                        '                        },\n',
                        '                        {\n',
                        '                            "description": "Change uiName",\n',
                        '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'WeaponUIName*' + "'" + '}.<TextProperty>",\n'
                        '                            "value": "TextProperty:' + "'" + uiName + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        },\n',
                        '                        {\n',
                        '                            "description": "Change Reload",\n',
                        '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'ReloadTime*' + "'" + '}.<FloatProperty>",\n'
                        '                            "value": "FloatProperty:' + "'" + str(stats[0]) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        },\n',
                        '                        {\n',
                        '                            "description": "Change Ammo",\n',
                        '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'WeaponAmmo*' + "'" + '}.<IntProperty>",\n'
                        '                            "value": "IntProperty:' + "'" + str(stats[1]) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        },\n',
                        '                        {\n',
                        '                            "description": "Change Proj",\n',
                        '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'MaxProjectile*' + "'" + '}.<IntProperty>",\n'
                        '                            "value": "IntProperty:' + "'" + str(stats[2]) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        },\n',
                        '                        {\n',
                        '                            "description": "Change Salvo",\n',
                        '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'MaxMultiLock*' + "'" + '}.<IntProperty>",\n'
                        '                            "value": "IntProperty:' + "'" + str(stats[3]) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        },\n',
                        '                        {\n',
                        '                            "description": "Change Range",\n',
                        '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'LockonRange*' + "'" + '}.<FloatProperty>",\n'
                        '                            "value": "FloatProperty:' + "'" + str(stats[4]) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        }\n',
                        '                    ]\n',
                        '                }',
                        ]
            dtp.writelines(statText)
            if w[1] == weaponsNames[len(weaponsNames)-1][1] and n == variants - 1:
                dtp.write('\n')
            else:
                dtp.write(',\n')

def missionOrderRando(seed):
    dtp = open(filepath, "a")
    random.seed(seed)

    missionIDs = missionIDList
    random.shuffle(missionIDs)
    openText = [
        '            "ProjectWingman/Content/ProjectWingman/Blueprints/Data/Levels/DB_ProjectWingmanLevelList.uexp": [\n',
        '                {\n',
        '                    "name": "Re-Order Missions",\n',
        '                    "patches": [\n',
    ]
    dtp.writelines(openText)

    for i, m in enumerate(missionNames):
        missionText = [
            '                        {\n',
            '                            "description": "",\n',
            '                            "template": "datatable:[' + "'" + m + "'" + '].[0].{' + "'ID*'" +'}.<StrProperty>",\n',
            '                            "value": "StrProperty:' + "'" + missionIDs[i] + "'" + '",\n',
            '                            "type": "propertyValue"\n',
            '                        },\n',
            '                        {\n',
            '                            "description": "",\n',
            '                            "template": "datatable:[' + "'" + m + "'" + '].[0].{' + "'NextLevelLink*'" + '}.<StrProperty>",\n',
            '                            "value": "StrProperty:' + "'" + missionPointers[missionIDs[i]] + "'" + '",\n',
            '                            "type": "propertyValue"\n',
            '                        }'
        ]
        dtp.writelines(missionText)
        if i < len(missionNames) - 1:
            dtp.write(',')
        dtp.write('\n')

    closeText = [
        '                    ]\n',
        '                }\n',
        '            ],\n'
    ]
    dtp.writelines(closeText)
    dtp.close()
"""
def npcAirRando(seed):
    print('hi')
    dtp = open(filepath, "a")
    random.seed(seed)

    openText = [
        '            "ProjectWingman/Content/ProjectWingman/Blueprints/Data/AircraftData/NPC/DAirUnitNPC.uexp": [\n',
    ]

    dtp.writelines(openText)

    for a in npcAicraft:
        stats = []
        for i, v in enumerate(naStatNames):
            stats.append(random.randint(naStatRanges[i][0], naStatRanges[i][1]))

        statText = ['                {\n',
                    '                    "name": "Set Stats",\n',
                    '                    "patches": [\n',
                    '                        {\n',
                    '                            "description": "Change BaseHp",\n',
                    '                            "template": "datatable:[' + "'" + a + "'" + '].[0].{' + "'" 'BaseHp*' + "'" + '}.<IntProperty>",\n'
                    '                            "value": "IntProperty:' + "'" + str(stats[0]) + "'" + '",\n',
                    '                            "type": "propertyValue"\n',
                    '                        },\n',
                    '                        {\n',
                    '                            "description": "Change Ammo",\n',
                    '                            "template": "datatable:[' + "'" + a + "'" + '].[0].{' + "'" 'RollSpeed*' + "'" + '}.<IntProperty>",\n'
                    '                            "value": "IntProperty:' + "'" + str(stats[1]) + "'" + '",\n',
                    '                            "type": "propertyValue"\n',
                    '                        },\n',
                    '                        {\n',
                    '                            "description": "Change Proj",\n',
                    '                            "template": "datatable:[' + "'" + a + "'" + '].[0].{' + "'" 'TurnSpeed*' + "'" + '}.<IntProperty>",\n'
                    '                            "value": "IntProperty:' + "'" + str(stats[2]) + "'" + '",\n',
                    '                            "type": "propertyValue"\n',
                    '                        },\n',
                    '                        {\n',
                    '                            "description": "Change Salvo",\n',
                    '                            "template": "datatable:[' + "'" + a + "'" + '].[0].{' + "'" 'YawSpeed*' + "'" + '}.<IntProperty>",\n'
                    '                            "value": "IntProperty:' + "'" + str(stats[3]) + "'" + '",\n',
                    '                            "type": "propertyValue"\n',
                    '                        },\n',
                    '                        {\n',
                    '                            "description": "Change Range",\n',
                    '                            "template": "datatable:[' + "'" + a + "'" + '].[0].{' + "'" 'DefaultSpeed*' + "'" + '}.<IntProperty>",\n'
                    '                            "value": "IntProperty:' + "'" + str(stats[4]) + "'" + '",\n',
                    '                            "type": "propertyValue"\n',
                    '                        },\n',
                    '                        {\n',
                    '                            "description": "Change Range",\n',
                    '                            "template": "datatable:[' + "'" + a + "'" + '].[0].{' + "'" 'Acceleration*' + "'" + '}.<IntProperty>",\n'
                    '                            "value": "IntProperty:' + "'" + str(stats[5]) + "'" + '",\n',
                    '                            "type": "propertyValue"\n',
                    '                        }\n',
                    '                    ]\n',
                    '                }',
                    ]
        dtp.writelines(statText)
        if a == npcAicraft[len(npcAicraft)-1]:
            dtp.write('\n')
        else:
            dtp.write(',\n')
    closeText = [
        '            ],\n'
    ]
    dtp.writelines(closeText)
    dtp.close()
"""


########################################################################################################################
##                                              GUI                                                                   ##
########################################################################################################################

window.title('Project Wingman Randomizer')
window.geometry('550x700+100+100')
window.config(bg='#303030')

seedGens = 0

# Displays the Settings Window
def openSettings():
    def saveSettings():
        try:
            boxstates()
            pStatStates()
            wStatStates()
            global unguidedChance
            unguidedChance = max(min(float(ugChance.get()), 1.0), 0.0)
            global OpSlotRanges
            a = int(OpsMin.get())
            b = int(OpsMax.get())
            attr = "Options per Slot"
            if a < 0:
                raise Exception("invalid value for '" + attr + "' minimum: " + str(a) + " < 0")
            if a > b:
                raise Exception("invalid stat range for '" + attr + "': " + str(a) + " > " + str(b))
            OpSlotRanges = [a,b]
            lblError = tk.Label(settings, text="\nSettings Saved", bg='#303030', fg='#e7530c', padx=300, font=('bold', 20),wraplength=800)
            lblError.grid(row=23, columnspan=7)
        except Exception as e:
            print(e)
            lblError = tk.Label(settings, text="\n"+str(e), bg='#303030', fg='#e7530c', padx=100, font=('bold', 20), wraplength=800)
            lblError.grid(row=23, columnspan=7)

    def boxstates():
        finalValue = []
        global weaponsSelected
        for x in TweaponsSelected:
            finalValue.append(x.get())
        weaponsSelected = finalValue
        print(weaponsSelected)

    def pStatStates():
        finalValue = []
        global pStatRanges
        for i, x in enumerate(TplaneStats):
            a = float(x[0].get())
            b = float(x[1].get())
            attr = pStatNames[i]
            if a < 0:
                raise Exception("invalid value for '" + attr + "' minimum: " + str(a) + " < 0")
            if a > b:
                if i != 0:
                    a = int(a)
                    b = int(b)
                raise Exception("invalid stat range for '" + attr + "': " + str(a) + " > " + str(b))
            if i == 0:
                finalValue.append([float(x[0].get()),float(x[1].get())])
            else:
                finalValue.append([int(x[0].get()), int(x[1].get())])
        pStatRanges = finalValue
        print(pStatRanges)

    def wStatStates():
        finalValue = []
        global wStatRanges
        for i, x in enumerate(TweaponStats):
            a = float(x[0].get())
            b = float(x[1].get())
            attr = wStatNames[i]
            if a < 0:
                raise Exception("invalid value for '" + attr + "' minimum: " + str(a) + " < 0")
            if a > b:
                if i != 5:
                    a = int(a)
                    b = int(b)
                raise Exception("invalid stat range for '" + attr + "': " + str(a) + " > " + str(b))
            if i == 5:
                finalValue.append([float(x[0].get()), float(x[1].get())])
            else:
                finalValue.append([int(x[0].get()), int(x[1].get())])
        wStatRanges = finalValue
        print(wStatRanges)

    settings = tk.Tk()
    settings.title('Project Wingman Randomizer Setings')
    settings.geometry('950x700+700+100')
    settings.config(bg='#303030')
    lHeading = tk.Label(settings,text='Advanced Settings', bg='#303030', fg='#e7530c',font=('bold', 26))
    lHeading.grid(row = 0, columnspan= 7)

    # ----------PLane Stats Select----------
    TplaneStats = [[tk.StringVar(settings, value=str(pStatRanges[0][0])), tk.StringVar(settings, value=str(pStatRanges[0][1]))],
                   [tk.StringVar(settings, value=str(pStatRanges[1][0])), tk.StringVar(settings, value=str(pStatRanges[1][1]))],
                   [tk.StringVar(settings, value=str(pStatRanges[2][0])), tk.StringVar(settings, value=str(pStatRanges[2][1]))],
                   [tk.StringVar(settings, value=str(pStatRanges[3][0])), tk.StringVar(settings, value=str(pStatRanges[3][1]))],
                   [tk.StringVar(settings, value=str(pStatRanges[4][0])), tk.StringVar(settings, value=str(pStatRanges[4][1]))],
                   [tk.StringVar(settings, value=str(pStatRanges[5][0])), tk.StringVar(settings, value=str(pStatRanges[5][1]))]]

    l3 = tk.Label(settings, text="Define Min and Max values for Aircraft Performance", bg='#303030', fg='#e7530c',
                  font=('bold', 20))
    l3.grid(row=1, columnspan=7)

    def createPlaneStatText():
        col = 0
        for x, y in zip(TplaneStats, pStatNames):
            label1 = tk.Label(settings, text=y, bg='#303030', fg='#e7530c', font=('bold', 15), wraplength=400)
            textMin = ttk.Entry(settings, textvariable=x[0])
            textMax = ttk.Entry(settings, textvariable=x[1])
            label1.grid(row=2, column=col)
            textMin.grid(row=3, column=col, padx=5)
            textMax.grid(row=4, column=col, padx=5)
            col = col + 1

    # ----------Weapon Select----------
    TweaponsSelected = [tk.BooleanVar(settings, value=weaponsSelected[i]) for i in range(len(WEAPONSMASTER))]

    l1 = tk.Label(settings, text = "Select Weapons", bg='#303030', fg='#e7530c', font=('bold', 20))
    l1.grid(row = 5, columnspan= 7)

    colHead = ["General", "Air to Air", "A2G Guided", "A2G Unguided", "Rockets", "Guns"]
    colLen = [6,4,5,6,5,5]

    def createCheckboxes():
        col = 0
        row = 0
        for x, y in zip (TweaponsSelected, WEAPONSNAMES):
            if row == 0:
                lh = tk.Label(settings, text=colHead[col], bg='#303030', fg='#e7530c', font=('bold', 15))
                lh.grid(row=6, column=col)

            check1_t1 = tk.Checkbutton(settings, text=y[2], variable=x, bg='#303030', fg='#e7530c', font=('bold', 12))
            check1_t1.grid(row = 7 + row, column = col, sticky='W')
            row = row + 1
            if row == colLen[col]:
                row = 0
                col = col + 1

    lblGuide = tk.Label(settings, text="Unguided Chance*", bg='#303030', fg='#e7530c', font=('bold', 15), wraplength=100)
    lblGuide.grid(row=6, column=6, rowspan=2)

    ugChance = tk.StringVar(settings, value=unguidedChance)
    text = ttk.Entry(settings, textvariable=ugChance)
    text.grid(row=8,column=6)

    lblOps = tk.Label(settings, text="Options per Slot", bg='#303030', fg='#e7530c', font=('bold', 15), wraplength=100)
    lblOps.grid(row=9, column=6, rowspan=2)
    OpsMin = tk.StringVar(settings, value=OpSlotRanges[0])
    text = ttk.Entry(settings, textvariable=OpsMin)
    text.grid(row=11, column=6)
    OpsMax = tk.StringVar(settings, value=OpSlotRanges[1])
    text = ttk.Entry(settings, textvariable=OpsMax)
    text.grid(row=12, column=6)

    # ----------Weapon Stats Select----------
    TweaponStats = [
        [tk.StringVar(settings, value=str(wStatRanges[0][0])), tk.StringVar(settings, value=str(wStatRanges[0][1]))],
        [tk.StringVar(settings, value=str(wStatRanges[1][0])), tk.StringVar(settings, value=str(wStatRanges[1][1]))],
        [tk.StringVar(settings, value=str(wStatRanges[2][0])), tk.StringVar(settings, value=str(wStatRanges[2][1]))],
        [tk.StringVar(settings, value=str(wStatRanges[3][0])), tk.StringVar(settings, value=str(wStatRanges[3][1]))],
        [tk.StringVar(settings, value=str(wStatRanges[4][0])), tk.StringVar(settings, value=str(wStatRanges[4][1]))],
        [tk.StringVar(settings, value=str(wStatRanges[5][0])), tk.StringVar(settings, value=str(wStatRanges[5][1]))],
        [tk.StringVar(settings, value=str(wStatRanges[6][0])), tk.StringVar(settings, value=str(wStatRanges[6][1]))]]

    l3 = tk.Label(settings, text="Define Min and Max values for Weapon Attributes", bg='#303030', fg='#e7530c', font=('bold', 20))
    l3.grid(row=14, columnspan=7)

    def createWeaponStatText():
        col=0
        for x, y in zip(TweaponStats, wStatNames):
            label1 = tk.Label(settings, text=y, bg='#303030', fg='#e7530c', font=('bold', 15), wraplength=400)
            textMin = ttk.Entry(settings, textvariable=x[0])
            textMax = ttk.Entry(settings, textvariable=x[1])
            label1.grid(row=15, column=col)
            textMin.grid(row=16, column=col, padx=5)
            textMax.grid(row=17, column=col, padx=5)
            col = col + 1

    """
    # ----------Misc Settings----------
    TrGuns = tk.BooleanVar(settings, value=rGuns)
    TallAoA = tk.BooleanVar(settings, value=allAoA)

    l4 = tk.Label(settings, text="Misc. Settings", bg='#303030', fg='#e7530c',font=('bold', 20))
    l4.grid(row=17, columnspan=7)

    c1 = tk.Checkbutton(settings, text='Randomize Internal Guns', variable=TrGuns, bg='#303030', fg='#e7530c', font=('bold', 15))
    c1.grid(row=18, column=0, columnspan=2)

    c1 = tk.Checkbutton(settings, text='Give all aircraft AoA Limiter', variable=TallAoA, bg='#303030', fg='#e7530c',font=('bold', 15))
    c1.grid(row=18, column=2, columnspan=2)
    """
    createPlaneStatText()
    createCheckboxes()
    createWeaponStatText()

    btn1 = tk.Button(settings, text="Save Settings", bg='#e7530c', command=saveSettings, width=25, font=('bold', 15))
    btn1.grid(row = 20, columnspan=7, pady=20)
    text1 = "* Defines the chance that unguided weapons will NOT become guided. 0 = 0%, 1 = 100%"

    lblInf1 = tk.Label(settings, text=text1, bg='#303030', fg='#e7530c', font=('bold', 15), wraplength=800)
    lblInf1.grid(row=21, columnspan=7)
    settings.mainloop()

l1 = tk.Label(text="Project Wingman Randomizer\n by FalconLuma", bg='#303030', fg='#e7530c', pady=(10),font=('bold', 26))
l1.pack()

l2 = tk.Label(text="Enter a seed or press the button to generate a random seed", bg='#303030', fg='#e7530c',
              font=('bold', 15), wraplength=400)
l2.pack()

t1 = tk.Text(window, height=1, width=40)
t1.pack()

b1 = tk.Button(window, text="Generate Random Seed", command=genSeed, bg='#303030', fg='#e7530c', font=('bold', 12))
b1.pack()

lblank1 = tk.Label(text="", bg='#303030', font=('', 8))
lblank1.pack()

l3 = tk.Label(text="Please select what attributes you would like to randomize:", bg='#303030', fg='#e7530c',
              font=('bold', 15), wraplength=500)
l3.pack()

c2 = tk.Checkbutton(window, text='Randomize Plane Performance', bg='#303030', fg='#e7530c', font=('bold', 15),
                    variable=rStats, onvalue=True, offvalue=False)
c2.pack()

c1 = tk.Checkbutton(window, text='Randomize Plane Weapons', bg='#303030', fg='#e7530c', font=('bold', 15),
                    variable=rLoad, onvalue=True, offvalue=False)
c1.pack()

c3 = tk.Checkbutton(window, text='Randomize Weapon Stats', bg='#303030', fg='#e7530c', font=('bold', 15),
                    variable=rWeps, onvalue=True, offvalue=False)
c3.pack()
c4 = tk.Checkbutton(window, text='Randomize Options/Slot', bg='#303030', fg='#e7530c', font=('bold', 15),
                    variable=rOpSlot, onvalue=True, offvalue=False)
c4.pack()
l4 = tk.Label(text="Enter the number of variations of each weapon", bg='#303030', fg='#e7530c',
              font=('bold', 15), wraplength=500)
l4.pack()

t2 = tk.Text(window, height=1, width=40)
t2.pack()

lblank2 = tk.Label(text="", bg='#303030', font=('', 8))
lblank2.pack()

b3 = tk.Button(window, text="Advanced Settings", bg='#e7530c', width=25, command=openSettings, font=('bold', 15))
b3.pack()

b2 = tk.Button(window, text="Press to Randomize", bg='#e7530c', width=25, command=runRando, font=('bold', 15))
b2.pack()

labelFinished = tk.Label(
    text="\nYour randomizer mod has been created\nPlease run ProjectSicario.exe\n\nYou can now close this program",
    bg='#303030', fg='#e7530c', font=('bold', 15), wraplength=500)

labelError = tk.Label(
    text="\nERROR: The mod file could not be created, ensure this program is located in your Project Wingman install folder and that the '~mods' folder exists in 'ProjectWingman\Content\Paks'",
    bg='#303030', fg='#e7530c', font=('bold', 15), wraplength=500)

window.mainloop()
