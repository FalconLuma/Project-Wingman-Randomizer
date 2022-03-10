import sys
import random
import StatRando
import WeaponRando

print('Please enter a seed or press enter to use a random seed')

# Read in the seed and remove the newline char

for line in sys.stdin:
    seed = line.strip('\n')
    break

# If no seed was entered create a random one
seed = ''
if seed == '':
    seed = int(random.randrange(sys.maxsize))
else:
    random.randrange(sys.maxsize)

# Print the seed back to the user
print('Your seed is: ' + str(seed))

dtp = open(r"../PWrando/ProjectWingman/sicario/pw-randomizer.dtp", "a")
dtpStart = ["{\n", ' "_meta": {\n', '  "DisplayName": "Weapon Randomizer: ' + str(seed) + '",\n', '  "Author": "FalconLuma"\n',
            ' },\n',
            ' "modParameters": {},\n', ' "mods": [{\n', '  "FilePatches": {},\n', '  "AssetPatches": {\n',]

dtp.writelines(dtpStart)
dtp.write('   "ProjectWingman/Content/ProjectWingman/Blueprints/Data/AircraftData/DB_Aircraft.uexp": [\n')
dtp.close()

rWeps = None
while rWeps == None:
    print("Do you want to randomize weapons for all planes? (Y/N)")
    for line in sys.stdin:
        answer = line.strip('\n')
        break
    if answer == 'y' or answer == 'Y':
        rWeps = True
    elif answer == 'n' or answer == 'N':
        rWeps = False
    else:
        print("Invalid input, please input answer as Y or N")

if rWeps:
    WeaponRando.weaponRando(seed)

rStats = None
while rStats == None:
    print("Do you want to randomize performance for all planes? (Y/N)")
    for line in sys.stdin:
        answer = line.strip('\n')
        break
    if answer == 'y' or answer == 'Y':
        rStats = True
    elif answer == 'n' or answer == 'N':
        rStats = False
    else:
        print("Invalid input, please input answer as Y or N")

if rStats:
    StatRando.statRando(seed)

dtp = open(r"../PWrando/ProjectWingman/sicario/pw-randomizer.dtp", "a")
dtp.write(']')
dtp.write('\n')
dtpEnd = ['  }\n', ' }]\n', '}']
dtp.writelines(dtpEnd)
dtp.close()