# -*- coding: utf-8 -*-

"""
@author: FalconLuma
"""

import random
import sys
import tkinter as tk
from enum import Enum

weaponsMaster = ['stdm', 'stdm2', 'mlaa', 'mlaa2', 'mlaa3', 'saa', 'mlag', 'mlag2', 'ugbs', 'ugbs3', 'ugbl',
                 'bdu16', 'gbs', 'gbs3', 'urs', 'urmb', 'urm', 'droptank', 'rgp', 'mgp', 'hgp', 'rgpd', 'sr', 'sr2',
                 'cgp', 'hvsm', 'hism', 'asm', 'hmaa', 'rdbm', 'eufb', 'bmlaa']

MINRESPONSE = 1.0
MINSPEED = 1000
MINACCEL = 25
MINROLL = 50
MINTURN = 50
MINYAW = 5

MAXRESPONSE = 7.0
MAXSPEED = 4000
MAXACCEL = 200
MAXROLL = 350
MAXTURN = 300
MAXYAW = 30

attrs = ['InterpSpeed', 'MaxSpeed', 'Acceleration', 'RollSpeed', 'TurnSpeed', 'YawSpeed']

filepath = r"./ProjectWingman/Content/Paks/~mods/pw-randomizer.dtp"


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
    SPEAR = [1,1,1, 'SPEAR']
    PWMK1 = [1,1,0, 'PW-001']

# Generates a random seed
def genSeed():
    t1.delete('1.0', 'end')
    seed = int(random.randrange(sys.maxsize))
    global seedGens
    seedGens = seedGens + 1
    print(seedGens)
    t1.insert('end',  str(seed))
    # Only allows one seed to be randomized
    b1.config(state='disabled')

# Manages running the randomizer
def runRando():
    seed = t1.get('1.0', 'end').strip('\n')

    global seedGens

    if seedGens == 0:
        # If the seed wasn't randomized runs a single rng to allow for random seeds to be repeatable
        random.randrange(sys.maxsize)

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
                  '            ],\n'
                  ]
    dtp.writelines(unlockText)

    dtp.write('            "ProjectWingman/Content/ProjectWingman/Blueprints/Data/AircraftData/DB_Aircraft.uexp": [\n')
    dtp.close()

    if rWeps.get():
        weaponRando(seed,nukes.get())

    if rStats.get():
        if rWeps.get():
            dtp = open(filepath, "a")
            dtp.write(',\n')
            dtp.close()
        statRando(seed)

    dtp = open(filepath, "a")
    dtpEnd = ['            ]\n',
              '        }\n',
              '    }]\n',
              '}']
    dtp.writelines(dtpEnd)
    dtp.close()

    # Display a message when the randomizer is finished

    labelFinished.pack()
    labelError.destroy()
    b2.config(state='disabled')

def weaponRando(seed, nukes):
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
                      '                            "template": "datatable:[' + "'" + PLANE.value[
                          3] + "'" + '''].[0].{'HardpointCompatibilityList*'}",\n''''',
                      '                            "value": "StrProperty:[' + "'" + 'stdm'
                      ]
        dtp.writelines(modTextTop)
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
                    if(not nukes and weapon == 'eufb'):
                        weapon = ''
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
                        '                            "template": "datatable:[' + "'" + PLANE.value[3] + "'" + '].[0].{'+ "'" + 'BaseStats*' + "'" + '}.{'+ "'" +'CannonType*'+ "'" +'}.<S_CannonType::>",\n',
                        '                            "value": "ByteProperty:' + "'" + 'S_CannonType::NewEnumerator' + str(random.randint(0,2)) + "'" + '",\n',
                        '                            "type": "propertyValue"\n',
                        '                        }\n'
                        ]
        dtp.writelines(gunRandoText)

        dtp.write('                    ]\n                }')
        if PLANE.value[3] != 'PW-001':
            dtp.write(',\n')

    dtp.close()


def statRando(seed):
    random.seed(seed)
    r = random.Random(seed)

    dtp = open(filepath, "a")

    # Iterate over all the planes
    for PLANE in PlaneInfo:
        response = round(random.uniform(MINRESPONSE, MAXRESPONSE), 1)
        speed = random.randint(MINSPEED, MAXSPEED)
        accel = random.randint(MINACCEL, MAXACCEL)
        roll = random.randint(MINROLL, MAXROLL)
        turn = random.randint(MINTURN, MAXTURN)
        yaw = random.randint(MINYAW, MAXYAW)

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
                '                            "template": "datatable:[' + "'" + PLANE.value[
                    3] + "'].[0].{'BaseStats*'}.{'" + attrs[i] + "*'}.<FloatProperty>" + '",\n'
                                                                                         '                            ''"value": "FloatProperty:' + str(
                    vals[i]) + '",\n',
                '                            "type": "propertyValue"\n',
                '                        }'
            ]
            dtp.writelines(modText)
            if i != 5:
                dtp.write(",\n")
            i = i + 1
        dtp.write('\n                    ]\n                }')
        if PLANE.value[3] != 'PW-001':
            dtp.write(',')
        dtp.write('\n')
    dtp.close()


########################################################################################################################
##                                              GUI                                                                   ##
########################################################################################################################

window = tk.Tk()
window.title('Project Wingman Randomizer')
window.geometry('500x600')
window.config(bg='#303030')

seedGens = 0

l1 = tk.Label(text="Project Wingman Randomizer\n by FalconLuma",bg='#303030',fg='#e7530c',pady=(10),font=('bold', 26))
l1.pack()

l2 = tk.Label(text="Enter a seed or press the button to generate a random seed",bg='#303030',fg='#e7530c',font=('bold', 15),wraplength=400)
l2.pack()

t1 = tk.Text(window, height=1, width=40)
t1.pack()

b1 = tk.Button(window, text="Create Random Seed", command=genSeed,bg='#303030',fg='#e7530c',font=('bold', 12))
b1.pack()

lblank1 = tk.Label(text="",bg='#303030',font=('',8))
lblank1.pack()

l3 = tk.Label(text="Please select what attributes you would like to randomize:",bg='#303030',fg='#e7530c',font=('bold', 15),wraplength=400)
l3.pack()

rWeps = tk.BooleanVar()
nukes = tk.BooleanVar()
rStats = tk.BooleanVar()
c1 = tk.Checkbutton(window, text='Randomize Plane Weapons',bg='#303030',fg='#e7530c',font=('bold', 15), variable=rWeps, onvalue=True, offvalue=False)
c1.pack()
c11 = tk.Checkbutton(window, text='Allow Nukes (EUFB)',bg='#303030',fg='#e7530c',font=('bold', 15), variable=nukes, onvalue=True, offvalue=False)
c11.pack()
c2 = tk.Checkbutton(window, text='Randomize Plane Performance',bg='#303030',fg='#e7530c',font=('bold', 15), variable=rStats, onvalue=True, offvalue=False)
c2.pack()

lblank2 = tk.Label(text="",bg='#303030',font=('',8))
lblank2.pack()

b2 = tk.Button(window, text="Press to Randomize",bg='#e7530c', width=25, command=runRando,font=('bold', 15))
b2.pack()

labelFinished = tk.Label(text="\nYour randomizer mod has been created\nPlease run ProjectSicario.exe\n\nYou can now close this program",bg='#303030',fg='#e7530c',font=('bold', 15),wraplength=400)

labelError = tk.Label(
        text="\nERROR: The mod file could not be created, ensure this program is located in your Project Wingman install folder and that the '~mods' folder exists in 'ProjectWingman\Content\Paks'",
        bg='#303030', fg='#e7530c', font=('bold', 15), wraplength=400)

window.mainloop()
