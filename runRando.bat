@echo off
python ".\PWrando\main.py"
set /p temp="Packing your randomizer mod"
python ".\u4pak-master\u4pak.py" pack "PW-randomizer-test_P.pak" "ProjectWingman"
set /p temp="Press enter to continue"
