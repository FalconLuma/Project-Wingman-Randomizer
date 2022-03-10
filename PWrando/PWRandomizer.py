import random
import sys
import tkinter as tk
from enum import Enum
import os

weaponsMaster = ['stdm', 'stdm2', 'mlaa', 'mlaa2', 'mlaa3', 'saa', 'mlag', 'mlag2', 'adm', 'ugbs', 'ugbs3', 'ugbl',
                 'bdu16', 'gbs', 'gbs3', 'urs', 'urmb', 'urm', 'droptank', 'rgp', 'mgp', 'hgp', 'rgps', 'sr', 'sr2',
                 'cgp', 'hvsm', 'hism', 'asm']

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

#Generates a random seed
def genSeed():
    t1.delete('1.0', 'end')
    seed = int(random.randrange(sys.maxsize))
    global seedGens
    seedGens = seedGens + 1
    print(seedGens)
    t1.insert('end', seed)
    # Only allows one seed to be randomized
    b1.config(state='disabled')

#Manages running the randomizer
def runRando():
    seed = t1.get('1.0','end').strip('\n')

    global seedGens

    if seedGens == 0:
        # If the seed wasn't randomized runs a single rng to allow for random seeds to be repeatable
        print('HI')
        random.randrange(sys.maxsize)

    dtp = open(r"./ProjectWingman/sicario/pw-randomizer.dtp", "r+")
    dtp.truncate(0)
    dtpStart = ["{\n", ' "_meta": {\n', '  "DisplayName": "Weapon Randomizer: ' + str(seed) + '",\n',
                '  "Author": "FalconLuma"\n',
                ' },\n',
                ' "modParameters": {},\n', ' "mods": [{\n', '  "FilePatches": {},\n', '  "AssetPatches": {\n', ]

    dtp.writelines(dtpStart)
    dtp.write('   "ProjectWingman/Content/ProjectWingman/Blueprints/Data/AircraftData/DB_Aircraft.uexp": [\n')
    dtp.close()

    if rWeps.get():
        weaponRando(seed)

    if rStats.get():
        statRando(seed)

    dtp = open(r"./ProjectWingman/sicario/pw-randomizer.dtp", "a")
    dtp.write(']')
    dtp.write('\n')
    dtpEnd = ['  }\n', ' }]\n', '}']
    dtp.writelines(dtpEnd)
    dtp.close()

def weaponRando(seed):
    random.seed(seed)
    r = random.Random(seed)

    numWeps = len(weaponsMaster)

    # Shuffle the main weapons list
    random.shuffle(weaponsMaster)

    dtp = open(r"./ProjectWingman/sicario/pw-randomizer.dtp", "a")


    # Iterate over all the planes
    for PLANE in PlaneInfo:
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

def statRando(seed):
    random.seed(seed)
    r = random.Random(seed)

    dtp = open(r"./ProjectWingman/sicario/pw-randomizer.dtp", "a")

    # Iterate over all the planes
    for PLANE in PlaneInfo:
        response = round(random.uniform(MINRESPONSE, MAXRESPONSE), 1)
        speed = random.randint(MINSPEED, MAXSPEED)
        accel = random.randint(MINACCEL, MAXACCEL)
        roll = random.randint(MINROLL, MAXROLL)
        turn = random.randint(MINTURN, MAXTURN)
        yaw = random.randint(MINYAW, MAXYAW)

        vals = [response,speed,accel,roll,turn,yaw]

        dtp.write('    {\n     "name": "' + PLANE.name + ' Random Stats",\n     "patches": [\n')

        i = 0
        while i < 6:
            dtp.write('      {\n       ''"description": "Modify ' + attrs[i] + '",\n       "template": "datatable:[' + "'" +
                PLANE.value[3] + "'].[0].{'BaseStats*'}.{'" + attrs[i] + "*'}.<FloatProperty>" + '",\n       '
                '"value": "FloatProperty:' + str(vals[i]) + '",\n       "type": "propertyValue"\n      }')
            if i != 5:
                dtp.write(", ")
            i = i + 1

        dtp.write('\n     ]\n    }')
        if PLANE.value[3] != 'ACG-01':
            dtp.write(',')
        dtp.write('\n')

    dtp.close()

########################################################################################################################
#####                                               GUI                                                            #####
########################################################################################################################

window = tk.Tk()
window.title('Project Wingman Randomizer')
window.geometry('500x500')
window.config(bg='#333333')

seedGens = 0

t1 = tk.Text(window,height=1,width=50)
t1.pack()

b1 = tk.Button(window, text = "Generate Seed", command=genSeed, )
b1.pack()


rWeps = tk.BooleanVar()
rStats = tk.BooleanVar()
c1 = tk.Checkbutton(window, text='Randomize Weapons', variable=rWeps, onvalue=True, offvalue=False)
c1.pack()
c2 = tk.Checkbutton(window, text='Randomize Stats', variable=rStats, onvalue=True, offvalue=False)
c2.pack()

b2 = tk.Button(window, text = "Press to Randomize", width = 25, command = runRando)
b2.pack()

window.mainloop()