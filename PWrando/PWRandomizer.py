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
from PIL import ImageTk, Image
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


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
    CR105C = [5, 6, 5, 'CF-105_2']
    MG21C = [3, 0, 0, 'MiG-21_2']
    ACCIPTERC = [6, 6, 6, 'AV-8_2']
    G10 = [8,8,8, 'A-10A']
    FF18 = [2,10,1,'F-18F']
    SK30 = [6, 3, 0, 'Su-30']
    W10B = [5,1,0,'J-10B']
    FT15 = [3,2,3,'FT-15']
    X16 = [5,5,0,'X-16']

UnreleasedPlanes = ['A-10A','F-18F','Su-30','J-10B','FT-15','X-16']

# Window declared here
window = tk.Tk()

WEAPONSNAMES = [['MSSL', 'stdm', 'STDM'], ['MSSL_Multi2', 'stdm2', 'STDM-2'], ['HVSM', 'hvsm', 'HVSM'],
                ['HISM', 'hism', 'HISM'], ['RDBM', 'rdbm', 'RDBM'], ['BMLAA', 'bmlaa', 'BML-U'],
                ['XMA4', 'mlaa', 'MLAA'], ['XMA4_Multi2', 'mlaa2', 'MLAA-2'], ['XMA4_Multi3', 'mlaa3', 'MLAA-3'],
                ['SAAM', 'saa', 'SAA'],
                ['ASM', 'asm', 'ASM'], ['AGM', 'mlag', 'MLAG'], ['AGM_Multi2', 'mlag2', 'MLAG-2'],
                ['GBS', 'gbs', 'GBS'], ['GBS_Multi3', 'gbs3', 'GBS-3'],
                ['UGBS', 'ugbs', 'UGBS'], ['UGBS_Multi3', 'ugbs3', 'UGBS-3'], ['UGBL', 'ugbl', 'UGBL'],
                ['DropTank', 'droptank', 'DT'], ['EUFB', 'eufb', 'EUFB'], ['BDU16', 'bdu16', 'BDU-16'],
                ['URS', 'urs', 'URS'], ['URM', 'urm', 'URM'], ['URMB', 'urmb', 'URMB'], ['SR', 'sr', 'SR'],
                ['SR-2', 'sr2', 'SR-2'],
                ['Gunpod_LITE', 'rgp', 'RGP'], ['Gunpod_MID', 'mgp', 'MGP'], ['Gunpod_HVY', 'hgp', 'HGP'],
                ['Gunpod_CAN', 'cgp', 'CGP'], ['RailgunGunpod', 'rgpd', 'RG']]

BWWEAPONSNAMES = [['MSSL', 'stdm', 'STDM'], ['MSSL_Multi2', 'stdm2', 'STDM-2'], ['HVSM', 'hvsm', 'HVSM'],
                ['HISM', 'hism', 'HISM'], ['RDBM', 'rdbm', 'RDBM'], ['BMLAA', 'bmlaa', 'BML-U'],
                ['XMA4', 'mlaa', 'MLAA'], ['XMA4_Multi2', 'mlaa2', 'MLAA-2'], ['XMA4_Multi3', 'mlaa3', 'MLAA-3'],
                ['SAAM', 'saa', 'SAA'], ['BW_XLAA', 'bwxlaa', 'XLAA'], ['QAAM', 'hmaa', 'HPAA'],
                ['ASM', 'asm', 'ASM'], ['AGM', 'mlag', 'MLAG'], ['AGM_Multi2', 'mlag2', 'MLAG-2'],
                ['GBS', 'gbs', 'GBS'], ['GBS_Multi3', 'gbs3', 'GBS-3'], ['BW_GBL','bwgbl','GBL'], ['BW_XASM', 'bwxasm', 'XASM'],
                ['UGBS', 'ugbs', 'UGBS'], ['UGBS_Multi3', 'ugbs3', 'UGBS-3'], ['UGBL', 'ugbl', 'UGBL'],
                ['DropTank', 'droptank', 'DT'], ['EUFB', 'eufb', 'EUFB'], ['BDU16', 'bdu16', 'BDU-16'],
                ['URS', 'urs', 'URS'], ['URM', 'urm', 'URM'], ['URMB', 'urmb', 'URMB'], ['BW_GRS', 'bwgrs', 'GRS'],
                ['SR', 'sr', 'ADM'], ['SR-2', 'sr2', 'ADM-2'],
                ['Gunpod_LITE', 'rgp', 'RGP'], ['Gunpod_MID', 'mgp', 'MGP'], ['Gunpod_HVY', 'hgp', 'HGP'],
                ['Gunpod_CAN', 'cgp', 'CGP'], ['RailgunGunpod', 'rgpd', 'RG']]

WEAPONSMASTER = ['stdm', 'stdm2', 'hvsm', 'hism', 'rdbm', 'bmlaa',
                 'mlaa', 'mlaa2', 'mlaa3', 'saa',
                 'asm', 'mlag', 'mlag2', 'gbs', 'gbs3',
                 'ugbs', 'ugbs3', 'ugbl', 'droptank', 'eufb', 'bdu16',
                 'urs', 'urm', 'urmb', 'sr', 'sr2', 'rgp', 'mgp', 'hgp', 'cgp', 'rgpd']

BWWEAPONSMASTER = ['stdm', 'stdm2', 'hvsm', 'hism', 'rdbm', 'bmlaa',
                 'mlaa', 'mlaa2', 'mlaa3', 'saa', 'bwxlaa', 'hmaa',
                 'asm', 'mlag', 'mlag2', 'gbs', 'gbs3', 'bwgbl', 'bwxasm',
                 'ugbs', 'ugbs3', 'ugbl', 'droptank', 'eufb', 'bdu16',
                 'urs', 'urm', 'urmb', 'bwgrs', 'sr', 'sr2',
                 'rgp', 'mgp', 'hgp', 'cgp', 'rgpd']

weaponsNames = []
weaponsMaster = []

weaponsSelected = [True, True, True, True, True, True,
                   True, True, True, True,
                   True, True, True, True, True,
                   True, True,True, True, False, True,
                   True, True, True, True, True,
                   True, True, True, True, True]

bwweaponsSelected = [True, True, True, True, True, True,
                     True, True, True, True, True, True,
                     True, True, True, True, True, True, True,
                     True, True, True, True, False, True,
                     True, True, True, True, True, True,
                     True, True, True, True, True]

# Plane Stat Ranges [Min, Max] Tuples
pStatNames = ['Response', 'Speed', 'Accel', 'Roll', 'Turn', 'Yaw']
pStatRanges = [[1.0, 7.0], [1000, 4000], [25, 200], [50, 350], [50, 300],
               [5, 30]]  # Response, Speed, Accel, Roll, Turn, Yaw

# Weapon Stat Ranges [Min, Max] Tuples
wStatNames = ['Reload', 'Ammunition', 'Loaded', 'Max Locks', 'Range', 'Gun Reload', 'Gun Ammo']
wStatRanges = [[3, 40], [8, 182], [1, 20], [1, 44], [2800, 12000], [0.01, 0.2],
               [320, 3800]]  # Reload, Ammo, Proj, Salvo, Range, GunReload, GunAmmo

unguidedChance = 0.5

attrs = ['InterpSpeed', 'MaxSpeed', 'Acceleration', 'RollSpeed', 'TurnSpeed', 'YawSpeed']

npcAircraft = ['AJS-37', 'F-18E', 'F-18F', 'F-18EADV', 'SU-27', 'MIG-31', 'F-15C', 'F-14D', 'F-22', 'F-16C', 'C-17',
               'C-17_Fast', 'C-17_Faster', 'B-52', 'AS-02', 'DV-204', 'FC-8', 'SU-37', 'F-15SMTD', 'SU-30', 'F-4E',
               'PW-01', 'J-10B', 'SU-25', 'Spear', 'CruiseMissile', 'CruiseMissile_Buff', 'CF-8', 'QGMk3', 'BCS4',
               'MIG-29', 'MIG-21', 'AV-8', 'CHIMERA', 'CIV-8']
naStatNames = ['BaseHP', 'RollSpeed', 'TurnSpeed', 'YawSpeed', 'DefaultSpeed', 'Acceleration']
naStatRanges = [[10, 400], [15, 300], [5, 200], [5, 200], [400, 1000], [100, 600]]

OpSlotRanges = [1, 11]

missionNames = ['C01_BlackFlag','C02_Frontiers', 'C03_Homestead', 'C04_Uphill', 'C05_Sirens', 'C06_MachineOfTheMantle',
                'C07_EminentDomain', 'C08_ClearSkies', 'C09_SteppingStone', 'C10_PillarsOfComm', 'C11_ColdWar',
                'C13_MidnightLight', 'C14_Valkyrie', 'C15_OpenSeason', 'C16_ConsequenceOf', 'C16B_Unfortunate',
                'C17_NoRespite', 'C18_Return', 'C19_RedSea', 'C20_Presidia', 'C22_Kings']

missionIDList = ['campaign_02', 'campaign_03', 'campaign_04', 'campaign_05', 'campaign_06', 'campaign_07','campaign_08',
                 'campaign_09', 'campaign_10', 'campaign_11', 'campaign_13', 'campaign_14', 'campaign_15','campaign_16',
                 'campaign_16.2', 'campaign_17', 'campaign_18', 'campaign_19', 'campaign_20', 'campaign_22']

missionIDList2 = ['campaign_02', 'campaign_03', 'campaign_04', 'campaign_05', 'campaign_06', 'campaign_07','campaign_08',
                 'campaign_09', 'campaign_10', 'campaign_11', 'campaign_13', 'campaign_14', 'campaign_15','campaign_16',
                 'campaign_16.2', 'campaign_17', 'campaign_18', 'campaign_19', 'campaign_20', 'campaign_22']

missionUnlockStrings = {
    'campaign_01': ['mission_01','freeflight','freemission','F-4E'],
    'campaign_02': ['mission_02', 'AJS-37','J-10B'],  # 'J10B'
    'campaign_03': ['mission_03', 'CF-105', 'Su-25'],
    'campaign_04': ['mission_04', 'MIG-31', 'F-16C'],
    'campaign_05': ['mission_05', 'F-14D', 'MiG-29'],
    'campaign_06': ['mission_06', 'A-10A', 'AV-8', 'X-16Z'],  # 'A-10A', 'X-16Z'
    'campaign_07': ['mission_07', 'F-18E', 'SU-27'],
    'campaign_08': ['mission_08', 'F-15C'],
    'campaign_09': ['mission_09', 'Su-30', 'F-18F'],  # 'Su-30', 'F-18F'
    'campaign_10': ['mission_10', 'F-15T'],  # 'F-15T'
    'campaign_11': ['mission_11'],
    'campaign_13': ['mission_13', 'ACG-01', 'F-15SMTD'],
    'campaign_14': ['mission_14'],
    'campaign_15': ['mission_15', 'SU-37'],
    'campaign_16': ['mission_16'],
    'campaign_16.2': ['mission_16.2'],
    'campaign_17': ['mission_17', 'F-22'],
    'campaign_18': ['mission_18'],
    'campaign_19': ['mission_19'],
    'campaign_20':['mission_20'],
    'campaign_22': ['campaignfinish', 'PW-001', 'SPEAR', 'mission_22']
}

missionPointers = dict()
for i, m in enumerate(missionIDList):
    if i < len(missionIDList) - 1:
        missionPointers[m] = missionIDList[i + 1]
    else:
        missionPointers[m] = 'ending'

filepath = r"./ProjectWingman/Content/Paks/~mods/pw-randomizer.dtp"

Unreleased = tk.BooleanVar()
rLoad = tk.BooleanVar()
rStats = tk.BooleanVar()
rWeps = tk.BooleanVar()
rOpSlot = tk.BooleanVar()
rMission = tk.BooleanVar()
repairUnlocks = tk.IntVar()
BWcompatibility = tk.BooleanVar()
rAirNpc = tk.BooleanVar(value=False)


# Generates a random seed
def gen_seed():
    t1.delete('1.0', 'end')
    seed = int(random.randrange(sys.maxsize))
    global seedGens
    seedGens = seedGens + 1
    t1.insert('end', str(seed))
    # Only allows one seed to be randomized
    b1.config(state='disabled')
    t1.config(state='disabled')


# Manages running the randomizer
def run_rando():
    print('Starting Randomizer')
    seed = t1.get('1.0', 'end').strip('\n')
    try:
        variants = int(t2.get('1.0', 'end').strip('\n'))
    except:
        variants = 1
    global seedGens

    if seedGens == 0:
        # If the seed wasn't generated, run a single rng to allow for generated seeds to be repeatable
        random.randrange(sys.maxsize)

    # Prepare weapons lists
    i = 0
    if BWcompatibility.get():
        wm = BWWEAPONSMASTER
        wn = BWWEAPONSNAMES
        ws = bwweaponsSelected
    else:
        wm = WEAPONSMASTER
        wn = WEAPONSNAMES
        ws = weaponsSelected
    while i < len(wm):
        if ws[i]:
            weaponsNames.append(wn[i])
            weaponsMaster.append(wm[i])
        i = i + 1

    # Try to open/create the dtp, at minimum the ~mods folder must exist, otherwise display an error message
    try:
        dtp = open(filepath, "w+")
        dtp.close()
    except:
        labelError.grid(row=20, columnspan=3)

    with open(filepath, "w+") as dtp:
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
        # Unlock normally unavailable weapons
        unlockText = ['            "ProjectWingman/Content/ProjectWingman/Blueprints/Data/Weapons/DWeaponDB.uexp": [\n',
                      '                {\n',
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
                      '                }'
                      ]
        dtp.writelines(unlockText)

    if rWeps.get():
        print('Randomizing Weapon Stats')
        with open(filepath, "a") as dtp:
            dtp.write(',\n')
        weapon_rando(seed, variants)

    # Close DB_Weapons and open DB_Aircraft
    with open(filepath, "a") as dtp:
        dtp.write('            ],\n')
        dtp.write('            "ProjectWingman/Content/ProjectWingman/Blueprints/Data/AircraftData/DB_Aircraft.uexp": [\n')

    if Unreleased.get():
        add_unreleased()

    if rLoad.get():
        print('Randomizing Loadouts')
        loadout_rando(seed)

    if rStats.get():
        print('Randomizing Aircraft Performance')
        if rLoad.get():
            with open(filepath, "a") as dtp:
                dtp.write(',\n')
        stat_rando(seed)

    # Close DB_Aircraft and open DB_ProjectWingmanLevelList
    with open(filepath, "a") as dtp:
        dtp.write('            ],\n')
        dtp.write('            "ProjectWingman/Content/ProjectWingman/Blueprints/Data/Levels/DB_ProjectWingmanLevelList.uexp": [\n')

    #unreleased_unlock_strings()
    if rMission.get():
        print('Randomizing Mission Order')
        mission_order_rando(seed)

    write_unlock_strings(seed)

    # Close DB_ProjectWingmanLevelList
    with open(filepath, "a") as dtp:
        dtp.write('            ]')

    if rAirNpc.get():
        print('Randomizing NPCs')
        with open(filepath, "a") as dtp:
            dtp.write(',\n')
        npc_air_rando(seed)

    # Close the dtp file
    with open(filepath, "a") as dtp:
        dtpEnd = ['\n        }\n',
                  '    }]\n',
                  '}']

        dtp.writelines(dtpEnd)
    # Display a message when the randomizer is finished
    print('Finished Randomizing')
    print('Depending on your settings Project Sicario Merger may take more than a minute to run')
    labelFinished.grid(row=20, columnspan=3)
    labelError.destroy()
    b2.config(state='disabled')


def add_unreleased():
    with open(filepath,"a") as dtp:
        for p in UnreleasedPlanes:
            unlockText = ['                {\n',
                          '                    "name": "' + p + '",\n',
                          '                    "patches": [\n',
                          '                        {\n',
                          '                            "description": "Make Available",\n',
                          '                            "template": "datatable:[' + "'" + p + "'" + '''].[0].{'ID_101*'}.{'Available*'}.<BoolProperty>",\n''',
                          '                            "value": "BoolProperty:true",\n',
                          '                            "type": "propertyValue"\n',
                          '                        },\n',
                          '                        {\n',
                          '                            "description": "Make Sellable",\n',
                          '                            "template": "datatable:[' + "'" + p + "'" + '''].[0].{'ID_101*'}.{'Sellable*'}.<BoolProperty>",\n''',
                          '                            "value": "BoolProperty:true",\n',
                          '                            "type": "propertyValue"\n',
                          '                        }\n',
                          '                    ]\n',
                          '                },\n',
                          ]
            dtp.writelines(unlockText)
            if p == 'J-10B':
                unlockText = ['                {\n',
                              '                    "name": "' + p + ' Info",\n',
                              '                    "patches": [\n',
                              #'                        {\n',
                              #'                            "description": "Name",\n',
                              #'                            "template": "datatable:[' + "'" + p + "'" + '''].[0].{'IndicatorName*'}.<TextProperty>",\n''',
                              #'                            "value": "TextProperty:W-10B",\n',
                              #'                            "type": "propertyValue"\n',
                              #'                        },\n',
                              '                        {\n',
                              '                            "description": "Price",\n',
                              '                            "template": "datatable:[' + "'" + p + "'" + '''].[0].{'Price*'}.<IntProperty>",\n''',
                              '                            "value": "IntProperty:' + "'" + str(5500) + "'" + '",\n',
                              '                            "type": "propertyValue"\n',
                              '                        }\n',
                              '                    ]\n',
                              '                },\n',
                              ]
                dtp.writelines(unlockText)


def loadout_rando(seed):
    random.seed(seed)

    num_weps = len(weaponsMaster)

    # Shuffle the main weapons list
    random.shuffle(weaponsMaster)

    with open(filepath, "a") as dtp:
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
                if rOpSlot.get():
                    if PLANE.value[s] == 0:
                        a = 0
                    else:
                        a = random.randint(OpSlotRanges[0], OpSlotRanges[1])
                else:
                    a = PLANE.value[s]
                w = [0 for _ in range(a)]
                i = 0
                while i < a and i < len(weaponsMaster):
                    # When no weapon is selected '' re-roll
                    # when a weapon is chosen remove it from the pool for this slot to avoid duplicates in the same slot
                    weapon = ''
                    while weapon == '':
                        wepNum = random.randint(0, num_weps - 1)
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
            if PLANE.value[3] != 'X-16':
                dtp.write(',\n')


def stat_rando(seed):
    random.seed(seed)

    with open(filepath, "a") as dtp:
        # Iterate over all the planes
        for PLANE in PlaneInfo:
            response = round(random.uniform(pStatRanges[0][0], pStatRanges[0][1]), 1)
            speed = random.randint(pStatRanges[1][0], pStatRanges[1][1])
            accel = random.randint(pStatRanges[2][0], pStatRanges[2][1])
            roll = random.randint(pStatRanges[3][0], pStatRanges[3][1])
            turn = random.randint(pStatRanges[4][0], pStatRanges[4][1])
            yaw = random.randint(pStatRanges[5][0], pStatRanges[5][1])

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
            if PLANE.value[3] != 'X-16':
                dtp.write(',')
            dtp.write('\n')


def weapon_rando(seed, variants):
    with open(filepath, "a") as dtp:
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
                if BWcompatibility.get():
                    ugList = ['ugbl', 'ugbs', 'ugbs3', 'droptank', 'eufb', 'bdu16', 'urs', 'urm', 'urmb']
                else:
                    ugList = ['ugbl', 'ugbs', 'ugbs3', 'droptank', 'eufb', 'bdu16', 'urs', 'urm', 'urmb', 'sr', 'sr2']
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
                        if w[1] in ugList:
                            c = round(random.uniform(0, 1), 2)
                            if unguidedChance >= c:
                                v = 0
                    stats.append(v)
                    i = i + 1

                statString = 'Reload: ' + str(stats[0]) + ',    ' + 'Ammo: ' + str(
                    stats[1]) + ',    ' + 'Loaded: ' + str(stats[2]) + ',    ' + 'Max Locks: ' + str(
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
                            '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'WeaponLongDescription*' + "'" + '}.<TextProperty>",\n',
                            '                            "value": "' + "'" + id + "_WeaponLongDescription':'" + statString + "'" + '",\n',
                            '                            "type": "textProperty"\n',
                            '                        },\n',
                            '                        {\n',
                            '                            "description": "Change uiName",\n',
                            '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'WeaponUIName*' + "'" + '}.<TextProperty>",\n',
                            '                            "value": "TextProperty:' + "'" + uiName + "'" + '",\n',
                            '                            "type": "propertyValue"\n',
                            '                        },\n',
                            '                        {\n',
                            '                            "description": "Change Reload",\n',
                            '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'ReloadTime*' + "'" + '}.<FloatProperty>",\n',
                            '                            "value": "FloatProperty:' + "'" + str(stats[0]) + "'" + '",\n',
                            '                            "type": "propertyValue"\n',
                            '                        },\n',
                            '                        {\n',
                            '                            "description": "Change Ammo",\n',
                            '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'WeaponAmmo*' + "'" + '}.<IntProperty>",\n',
                            '                            "value": "IntProperty:' + "'" + str(stats[1]) + "'" + '",\n',
                            '                            "type": "propertyValue"\n',
                            '                        },\n',
                            '                        {\n',
                            '                            "description": "Change Proj",\n',
                            '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'MaxProjectile*' + "'" + '}.<IntProperty>",\n',
                            '                            "value": "IntProperty:' + "'" + str(stats[2]) + "'" + '",\n',
                            '                            "type": "propertyValue"\n',
                            '                        },\n',
                            '                        {\n',
                            '                            "description": "Change Salvo",\n',
                            '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'MaxMultiLock*' + "'" + '}.<IntProperty>",\n',
                            '                            "value": "IntProperty:' + "'" + str(stats[3]) + "'" + '",\n',
                            '                            "type": "propertyValue"\n',
                            '                        },\n',
                            '                        {\n',
                            '                            "description": "Change Range",\n',
                            '                            "template": "datatable:[' + "'" + id + "'" + '].[0].{' + "'" 'LockonRange*' + "'" + '}.<FloatProperty>",\n',
                            '                            "value": "FloatProperty:' + "'" + str(stats[4]) + "'" + '",\n',
                            '                            "type": "propertyValue"\n',
                            '                        }\n',
                            '                    ]\n',
                            '                }',
                            ]
                dtp.writelines(statText)
                if w[1] == weaponsNames[len(weaponsNames) - 1][1] and n == variants - 1:
                    dtp.write('\n')
                else:
                    dtp.write(',\n')


def unreleased_unlock_strings():
    with open(filepath, "a") as dtp:
        openText = [
            '                {\n',
            '                    "name": "Update Unlock Strings",\n',
            '                    "patches": [\n',
        ]
        dtp.writelines(openText)
        mIdL = ['campaign_01']
        mIdL.extend(missionIDList)
        for i, m in enumerate(missionNames):
            unlockText = [
                '                        {\n',
                '                            "description": "",\n',
                '                            "template": "datatable:[' + "'" + m + "'" + '].[0].{' + "'UnlocksStringReward*'" + '}",\n',
                '                            "value": "StrProperty:' + str(missionUnlockStrings[mIdL[i]]) + '",\n',
                '                            "type": "arrayPropertyValue"\n',
                '                        }',
            ]
            dtp.writelines(unlockText)

            if i < len(missionNames) - 1:
                dtp.write(',')
            dtp.write('\n')

        closeText = [
            '                    ]\n',
            '                }\n',
        ]
        dtp.writelines(closeText)


def mission_order_rando(seed):
    with open(filepath, "a") as dtp:
        random.seed(seed)

        missionIDs = missionIDList
        random.shuffle(missionIDs)
        #print(missionIDList)
        openText = [
            '                {\n',
            '                    "name": "Re-Order Missions",\n',
            '                    "patches": [\n',
        ]
        dtp.writelines(openText)

        for i, m in enumerate(missionNames):
            if i == 0:
                pass
            else:
                missionText = [
                    '                        {\n',
                    '                            "description": "",\n',
                    '                            "template": "datatable:[' + "'" + m + "'" + '].[0].{' + "'ID*'" + '}.<StrProperty>",\n',
                    '                            "value": "StrProperty:' + "'" + missionIDs[i-1] + "'" + '",\n',
                    '                            "type": "propertyValue"\n',
                    '                        },\n',
                    '                        {\n',
                    '                            "description": "",\n',
                    '                            "template": "datatable:[' + "'" + m + "'" + '].[0].{' + "'NextLevelLink*'" + '}.<StrProperty>",\n',
                    '                            "value": "StrProperty:' + "'" + missionPointers[missionIDs[i-1]] + "'" + '",\n',
                    '                            "type": "propertyValue"\n',
                    '                        }'
                ]
                dtp.writelines(missionText)

#            if repairUnlocks.get():
#                unlockText = [
#                    ',\n',
#                    '                        {\n',
#                    '                            "description": "",\n',
#                    '                            "template": "datatable:[' + "'" + m + "'" + '].[0].{' + "'UnlocksStringReward*'" + '}",\n',
#                    '                            "value": "StrProperty:' + str(missionUnlockStrings[missionIDs[i]]) + '",\n',
#                    '                            "type": "arrayPropertyValue"\n',
#                    '                        }',
#                ]
#                dtp.writelines(unlockText)

            if (not i == 0) and i < len(missionNames) - 1:
                dtp.write(',')
            dtp.write('\n')

        closeText = [
            '                    ]\n',
            '                }\n',
        ]
        dtp.writelines(closeText)


def unlock_rando(seed):

    random.seed(seed)

    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    unlockStrings = {
        'campaign_01': ['mission_01','freeflight','freemission'],
        'campaign_02': ['mission_02'],
        'campaign_03': ['mission_03'],
        'campaign_04': ['mission_04'],
        'campaign_05': ['mission_05'],
        'campaign_06': ['mission_06'],
        'campaign_07': ['mission_07'],
        'campaign_08': ['mission_08'],
        'campaign_09': ['mission_09'],
        'campaign_10': ['mission_10'],
        'campaign_11': ['mission_11'],
        'campaign_13': ['mission_13'],
        'campaign_14': ['mission_14'],
        'campaign_15': ['mission_15'],
        'campaign_16': ['mission_16'],
        'campaign_16.2': ['mission_16.2'],
        'campaign_17': ['mission_17'],
        'campaign_18': ['mission_18'],
        'campaign_19': ['mission_19'],
        'campaign_20':['mission_20'],
        'campaign_22': ['campaignfinish', 'mission_22']
    }

    planelist = []
    for p in PlaneInfo:
        ID = p.value[3]
        if ID == 'X-16':
            ID = 'X-16Z'
        elif ID == 'FT-15':
            ID = 'F-15T'
        if ID not in ['T-21', 'TF-4E','MiG-21','CF-105_2','MiG-21_2','AV-8_2']:
            planelist.append(ID)

    random.shuffle(planelist)
    m = 0
    mIdL = ['campaign_01']
    mIdL.extend(missionIDList2)
    while len(planelist) > 0:
        if counts[m] < 2:
            addPlane = random.choice([True,False])
            if addPlane:
                newPlane = planelist.pop(0)
                counts[m] = counts[m] + 1
                key = mIdL[m]
                unlckStr = unlockStrings[key]
                unlckStr.append(newPlane)
                unlockStrings[key] = unlckStr

        m = (m + 1) % 20

    return unlockStrings


def write_unlock_strings(seed):
    with open(filepath, "a") as dtp:
        #print(repairUnlocks.get())
        unlockStrings = missionUnlockStrings
        mIdL = ['campaign_01']
        if repairUnlocks.get() == 1:
            mIdL.extend(missionIDList2)
        else:
            mIdL.extend(missionIDList)
        #mIdL)
        #if repairUnlocks.get() == 1:
        #    pass
        #else:

        if rMission.get():
            openText = [
                '                ,{\n'
                '                    "name": "Update Unlcoks",\n',
                '                    "patches": [\n',
            ]
        else:
            openText = [
                '                {\n'
                '                    "name": "Update Unlcoks",\n',
                '                    "patches": [\n',
            ]
        dtp.writelines(openText)
        if repairUnlocks.get() == 2:

            unlockStrings = unlock_rando(seed)
        for i, m in enumerate(missionNames):
            unlockText = [
                '                        {\n',
                '                            "description": "",\n',
                '                            "template": "datatable:[' + "'" + m + "'" + '].[0].{' + "'UnlocksStringReward*'" + '}",\n',
                '                            "value": "StrProperty:' + str(unlockStrings[mIdL[i]]) + '",\n',
                '                            "type": "arrayPropertyValue"\n',
                '                        }',
            ]
            dtp.writelines(unlockText)

            if i < len(missionNames) - 1:
                dtp.write(',')
            dtp.write('\n')
        dtp.write('                    ]\n')

        closeText = [
            '                }\n',
        ]
        dtp.writelines(closeText)


def npc_air_rando(seed):
    with open(filepath, "a") as dtp:
        random.seed(seed)

        openText = [
            '            "ProjectWingman/Content/ProjectWingman/Blueprints/Data/AircraftData/NPC/DAirUnitNPC.uexp": [\n',
        ]

        dtp.writelines(openText)
        for a in npcAircraft:
            stats = []
            for i, v in enumerate(naStatNames):
                stats.append(random.randint(naStatRanges[i][0], naStatRanges[i][1]))

            statText = ['                {\n',
                        '                    "name": "Set Stats",\n',
                        '                    "patches": [\n',
                        '                        {\n',
                        '                            "description": "Change BaseHp",\n',
                        '                            "template": "datatable:[' + "'" + a + "'" + '].[0].{' + "'" 'BaseHp*' + "'" + '}.<IntProperty>",\n',
                        '                            "value": "FloatProperty:' + "'" + str(1000000.0) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        },\n',
                        '                        {\n',
                        '                            "description": "Change Ammo",\n',
                        '                            "template": "datatable:[' + "'" + a + "'" + '].[0].{' + "'" 'RollSpeed*' + "'" + '}.<IntProperty>",\n',
                        '                            "value": "IntProperty:' + "'" + str(stats[1]) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        },\n',
                        '                        {\n',
                        '                            "description": "Change Proj",\n',
                        '                            "template": "datatable:[' + "'" + a + "'" + '].[0].{' + "'" 'TurnSpeed*' + "'" + '}.<IntProperty>",\n',
                        '                            "value": "IntProperty:' + "'" + str(stats[2]) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        },\n',
                        '                        {\n',
                        '                            "description": "Change Salvo",\n',
                        '                            "template": "datatable:[' + "'" + a + "'" + '].[0].{' + "'" 'YawSpeed*' + "'" + '}.<IntProperty>",\n',
                        '                            "value": "IntProperty:' + "'" + str(stats[3]) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        },\n',
                        '                        {\n',
                        '                            "description": "Change Range",\n',
                        '                            "template": "datatable:[' + "'" + a + "'" + '].[0].{' + "'" 'DefaultSpeed*' + "'" + '}.<IntProperty>",\n',
                        '                            "value": "IntProperty:' + "'" + str(stats[4]) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        },\n',
                        '                        {\n',
                        '                            "description": "Change Range",\n',
                        '                            "template": "datatable:[' + "'" + a + "'" + '].[0].{' + "'" 'Acceleration*' + "'" + '}.<IntProperty>",\n',
                        '                            "value": "IntProperty:' + "'" + str(stats[5]) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        }\n',
                        '                    ]\n',
                        '                }',
                        ]
            dtp.writelines(statText)
            if a == npcAircraft[len(npcAircraft) - 1]:
                dtp.write('\n')
            else:
                dtp.write(',\n')
        closeText = [
            '            ]\n'
        ]
        dtp.writelines(closeText)


########################################################################################################################
#                                                         GUI                                                          #
########################################################################################################################

if __name__ == "__main__":
    print('Opening Randomizer')

    window.title('Project Wingman Randomizer')
    window.geometry('550x800+100+100')
    window.config(bg='#303030')

    seedGens = 0

    # Displays the Settings Window
    def open_settings():
        def save_settings():
            try:
                boxstates()
                p_stat_states()
                w_stat_states()
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
                OpSlotRanges = [a, b]
                lblError = tk.Label(settings, text="\nSettings Saved", bg='#303030', fg='#e7530c', padx=300,
                                    font=('bold', 20), wraplength=800)
                lblError.grid(row=23, columnspan=7)
            except Exception as e:
                print(e)
                lblError = tk.Label(settings, text="\n" + str(e), bg='#303030', fg='#e7530c', padx=100,
                                    font=('bold', 20), wraplength=800)
                lblError.grid(row=23, columnspan=7)

        def boxstates():
            finalValue = []
            global weaponsSelected
            for x in TweaponsSelected:
                finalValue.append(x.get())
            weaponsSelected = finalValue
            #print(weaponsSelected)

        def p_stat_states():
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
                    finalValue.append([float(x[0].get()), float(x[1].get())])
                else:
                    finalValue.append([int(x[0].get()), int(x[1].get())])
            pStatRanges = finalValue
            #print(pStatRanges)

        def w_stat_states():
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
            #print(wStatRanges)

        settings = tk.Tk()
        settings.title('Project Wingman Randomizer Settings')
        settings.geometry('950x700+700+100')
        settings.config(bg='#303030')
        lHeading = tk.Label(settings, text='Advanced Settings', bg='#303030', fg='#e7530c', font=('bold', 26))
        lHeading.grid(row=0, columnspan=7)

        # ----------PLane Stats Select----------
        TplaneStats = [[tk.StringVar(settings, value=str(pStatRanges[0][0])),
                        tk.StringVar(settings, value=str(pStatRanges[0][1]))],
                       [tk.StringVar(settings, value=str(pStatRanges[1][0])),
                        tk.StringVar(settings, value=str(pStatRanges[1][1]))],
                       [tk.StringVar(settings, value=str(pStatRanges[2][0])),
                        tk.StringVar(settings, value=str(pStatRanges[2][1]))],
                       [tk.StringVar(settings, value=str(pStatRanges[3][0])),
                        tk.StringVar(settings, value=str(pStatRanges[3][1]))],
                       [tk.StringVar(settings, value=str(pStatRanges[4][0])),
                        tk.StringVar(settings, value=str(pStatRanges[4][1]))],
                       [tk.StringVar(settings, value=str(pStatRanges[5][0])),
                        tk.StringVar(settings, value=str(pStatRanges[5][1]))]]

        l3 = tk.Label(settings, text="Define Min and Max values for Aircraft Performance", bg='#303030', fg='#e7530c',
                      font=('bold', 20))
        l3.grid(row=1, columnspan=7)

        def create_plane_stat_text():
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
        if BWcompatibility.get():
            wm = BWWEAPONSMASTER
            wn = BWWEAPONSNAMES
            ws = bwweaponsSelected
            colLen = [6, 6, 7, 6, 6, 5]
        else:
            wm = WEAPONSMASTER
            wn = WEAPONSNAMES
            ws = weaponsSelected
            colLen = [6, 4, 5, 6, 5, 5]
        TweaponsSelected = [tk.BooleanVar(settings, value=ws[i]) for i in range(len(wm))]

        l1 = tk.Label(settings, text="Select Weapons", bg='#303030', fg='#e7530c', font=('bold', 20))
        l1.grid(row=5, columnspan=7)

        colHead = ["General", "Air to Air", "A2G Guided", "A2G Unguided", "Rockets", "Guns"]
        def create_checkboxes():
            col = 0
            row = 0
            for x, y in zip(TweaponsSelected, wn):
                if row == 0:
                    lh = tk.Label(settings, text=colHead[col], bg='#303030', fg='#e7530c', font=('bold', 15))
                    lh.grid(row=6, column=col)

                check1_t1 = tk.Checkbutton(settings, text=y[2], variable=x, bg='#303030', fg='#e7530c',
                                           font=('bold', 12))
                check1_t1.grid(row=7 + row, column=col, sticky='W')
                row = row + 1
                if row == colLen[col]:
                    row = 0
                    col = col + 1

        lblGuide = tk.Label(settings, text="Unguided Chance", bg='#303030', fg='#e7530c', font=('bold', 15),
                            wraplength=100)
        lblGuide.grid(row=6, column=6, rowspan=2)

        ugChance = tk.StringVar(settings, value=str(unguidedChance))
        text = ttk.Entry(settings, textvariable=ugChance)
        text.grid(row=8, column=6)

        lblOps = tk.Label(settings, text="Options per Slot", bg='#303030', fg='#e7530c', font=('bold', 15),
                          wraplength=100)
        lblOps.grid(row=9, column=6, rowspan=2)
        OpsMin = tk.StringVar(settings, value=str(OpSlotRanges[0]))
        text = ttk.Entry(settings, textvariable=OpsMin)
        text.grid(row=11, column=6)
        OpsMax = tk.StringVar(settings, value=str(OpSlotRanges[1]))
        text = ttk.Entry(settings, textvariable=OpsMax)
        text.grid(row=12, column=6)

        # ----------Weapon Stats Select----------
        TweaponStats = [
            [tk.StringVar(settings, value=str(wStatRanges[0][0])),
             tk.StringVar(settings, value=str(wStatRanges[0][1]))],
            [tk.StringVar(settings, value=str(wStatRanges[1][0])),
             tk.StringVar(settings, value=str(wStatRanges[1][1]))],
            [tk.StringVar(settings, value=str(wStatRanges[2][0])),
             tk.StringVar(settings, value=str(wStatRanges[2][1]))],
            [tk.StringVar(settings, value=str(wStatRanges[3][0])),
             tk.StringVar(settings, value=str(wStatRanges[3][1]))],
            [tk.StringVar(settings, value=str(wStatRanges[4][0])),
             tk.StringVar(settings, value=str(wStatRanges[4][1]))],
            [tk.StringVar(settings, value=str(wStatRanges[5][0])),
             tk.StringVar(settings, value=str(wStatRanges[5][1]))],
            [tk.StringVar(settings, value=str(wStatRanges[6][0])),
             tk.StringVar(settings, value=str(wStatRanges[6][1]))]]

        l3 = tk.Label(settings, text="Define Min and Max values for Weapon Attributes", bg='#303030', fg='#e7530c',
                      font=('bold', 20))
        l3.grid(row=16, columnspan=7)

        def create_weapon_stat_text():
            col = 0
            for x, y in zip(TweaponStats, wStatNames):
                label1 = tk.Label(settings, text=y, bg='#303030', fg='#e7530c', font=('bold', 15), wraplength=400)
                textMin = ttk.Entry(settings, textvariable=x[0])
                textMax = ttk.Entry(settings, textvariable=x[1])
                label1.grid(row=17, column=col)
                textMin.grid(row=18, column=col, padx=5)
                textMax.grid(row=19, column=col, padx=5)
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

        create_plane_stat_text()
        create_checkboxes()
        create_weapon_stat_text()

        btn1 = tk.Button(settings, text="Save Settings", bg='#e7530c', command=save_settings, width=25,
                         font=('bold', 15))
        btn1.grid(row=22 , columnspan=7, pady=20)
        settings.mainloop()

    canvas_width = 550
    width = 550
    height = int((width / 5348) * 2362)
    canvas_height = 150
    c1 = tk.Canvas(width=canvas_width, height=canvas_height, bg='#303030', border=0, highlightthickness=0)
    c1.grid(row=0, columnspan=3)
    #c1.pack()
    img = Image.open(resource_path('Banner1.png'))

    img = img.resize((width, height))
    img = ImageTk.PhotoImage(img)
    c1.create_image(canvas_width / 2, canvas_height / 2, anchor='c', image=img)

    # l1 = tk.Label(text="Project Wingman Randomizer\n by FalconLuma", bg='#303030', fg='#e7530c', pady=(10),font=('bold', 26))
    # l1.pack()

    l2 = tk.Label(text="Enter a seed or press the button to generate a random seed",
                  bg='#303030', fg='#e7530c',font=('bold', 15), wraplength=400)
    l2.grid(row=1, columnspan=3)
    frameSeed = tk.Frame(window,bg='#303030')
    frameSeed.grid(row=2, columnspan=3)

    t1 = tk.Text(frameSeed, height=1, width=35)
    t1.grid(row=0, columnspan=2, sticky='E')

    b1 = tk.Button(frameSeed, text="Random Seed", command=gen_seed,
                   bg='#303030', fg='#e7530c', font=('bold', 12))
    b1.grid(row=0, column=2, sticky='W')

    lblank1 = tk.Label(text="", bg='#303030', font=('', 8))
    lblank1.grid(row=4, columnspan=3)

    # Aircraft Rando Settings
    l3 = tk.Label(text="Player Aircraft Randomization:",
                  bg='#303030', fg='#e7530c', font=('bold', 20), wraplength=500)
    l3.grid(row=6, columnspan=3)

    c2 = tk.Checkbutton(window, text='Performance', bg='#303030', fg='#e7530c', font=('bold', 15),
                        variable=rStats, onvalue=True, offvalue=False)
    c2.grid(row=7, column=0, sticky='E')

    c1 = tk.Checkbutton(window, text='Loadouts', bg='#303030', fg='#e7530c', font=('bold', 15),
                        variable=rLoad, onvalue=True, offvalue=False)
    c1.grid(row=7, column=1)

    c4 = tk.Checkbutton(window, text='Options/Slot', bg='#303030', fg='#e7530c', font=('bold', 15),
                        variable=rOpSlot, onvalue=True, offvalue=False)
    c4.grid(row=7, column=2,sticky='W')

    lblank1 = tk.Label(text="", bg='#303030', font=('', 4))
    lblank1.grid(row=8, columnspan=3)
    # Weapon Rando Settings
    l4 = tk.Label(text="Player Weapon Randomization:",
                  bg='#303030', fg='#e7530c', font=('bold', 20), wraplength=500)
    l4.grid(row=9, columnspan=3)

    framWep = tk.Frame(window, bg='#303030')
    framWep.grid(row=10,columnspan=3)

    c3 = tk.Checkbutton(framWep, text='Stats', bg='#303030', fg='#e7530c', font=('bold', 15),
                        variable=rWeps, onvalue=True, offvalue=False)
    c3.grid(row=0, column=0, sticky='E')

    frameVar = tk.Frame(framWep, bg='#303030')
    frameVar.grid(row=0, column=1, sticky='W')

    l4 = tk.Label(frameVar, text="      Variants:", bg='#303030', fg='#e7530c',
                  font=('bold', 15), wraplength=500)
    l4.grid(row=0, column=0, sticky='E')

    t2 = tk.Text(frameVar, height=1, width=10)
    t2.grid(row=0, column=1, sticky='W')

    lblank1 = tk.Label(text="", bg='#303030', font=('', 4))
    lblank1.grid(row=11, columnspan=3)

    # Mission Order
    l5 = tk.Label(text="Mission and Unlock Order:",
                  bg='#303030', fg='#e7530c', font=('bold', 20), wraplength=500)
    l5.grid(row=12, columnspan=3)

    c5 = tk.Checkbutton(window, text='Randomize Mission Order', bg='#303030', fg='#e7530c', font=('bold', 15),
                        variable=rMission, onvalue=True, offvalue=False)
    c5.grid(row=13, columnspan=3)

    #Unlock Order
    frameUn = tk.Frame(window, bg='#303030')
    frameUn.grid(row=14, columnspan=3)

    lun = tk.Label(frameUn, text="Unlock Order:", bg='#303030', fg='#e7530c', font=('bold', 15))
    lun.grid(row=0, column=0)

    r1 = tk.Radiobutton(frameUn, text='Normal', bg='#303030', fg='#e7530c', font=('bold', 15),
                        variable=repairUnlocks, value=0)
    r1.grid(row=0, column=1)
    r2 = tk.Radiobutton(frameUn, text='Mission', bg='#303030', fg='#e7530c', font=('bold', 15),
                        variable=repairUnlocks, value=1)
    r2.grid(row=0, column=2)
    r2 = tk.Radiobutton(frameUn, text='Random', bg='#303030', fg='#e7530c', font=('bold', 15),
                        variable=repairUnlocks, value=2)
    r2.grid(row=0, column=3)

    lblank1 = tk.Label(text="", bg='#303030', font=('', 4))
    lblank1.grid(row=15, columnspan=3)

    #Additional Content
    l6 = tk.Label(text="Additional Content:",bg='#303030', fg='#e7530c', font=('bold', 20), wraplength=500)
    l6.grid(row=16, columnspan=3)

    frameAdd = tk.Frame(window, bg='#303030')
    frameAdd.grid(row=17, columnspan=3)

    cU = tk.Checkbutton(frameAdd, text='Unreleased Planes', bg='#303030', fg='#e7530c', font=('bold', 15),
                        variable=Unreleased, onvalue=True, offvalue=False)
    cU.grid(row=0, column=0)

    c7 = tk.Checkbutton(frameAdd, text='Balanced Wingman Compatibility', bg='#303030', fg='#e7530c', font=('bold', 15),
                        variable=BWcompatibility, onvalue=True, offvalue=False)
    c7.grid(row=0, column=1)

    lblank2 = tk.Label(text="", bg='#303030', font=('', 4))
    lblank2.grid(row=18, columnspan=3)

    b3 = tk.Button(window, text="Advanced Settings", bg='#e7530c', width=25, command=open_settings, font=('bold', 15))
    b3.grid(row=19, columnspan=3)

    b2 = tk.Button(window, text="Press to Randomize", bg='#e7530c', width=25, command=run_rando, font=('bold', 15))
    b2.grid(row=20, columnspan=3)

    labelFinished = tk.Label(
        text="\nYour randomizer mod has been created\nPlease run ProjectSicario.exe\n\nYou can now close this program",
        bg='#303030', fg='#e7530c', font=('bold', 15), wraplength=500)

    labelError = tk.Label(
        text="\nERROR: The mod file could not be created, ensure this program is located in your Project Wingman "
             "install folder and that the '~mods' folder exists in 'ProjectWingman/Content/Paks'",
        bg='#303030', fg='#e7530c', font=('bold', 15), wraplength=500)

    window.mainloop()
