import sys
import random
import PLANEINFO

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

seed = sys.argv[1]

random.seed(seed)
r = random.Random(seed)

dtp = open(r".\ProjectWingman\sicario\pw-randomizer.dtp", "a")



# Iterate over all the planes
for PLANE in PLANEINFO.PlaneInfo:
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
        dtp.write('{\n       ''"description": "Modify ' + attrs[i] + '",\n       "template": "datatable:[' + "'" +
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
