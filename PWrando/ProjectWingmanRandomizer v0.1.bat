@echo off

del /q .\ProjectWingman\sicario\*

echo Welcome to the Project Wingman Randomizer mod by FalconLuma
echo.

python ".\main.py"

echo.
echo Packing your randomizer mod as 'PW-Randomizer_P.pak'

python ".\u4pak-master\u4pak.py" pack "PW-Randomizer_P.pak" ".\ProjectWingman"

echo.
echo Your mod has been packed, place the .pak file in the '~mods' folder and run ProjectSicario.exe
set /p temp="Press enter to finish"
