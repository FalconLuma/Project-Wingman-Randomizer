Project Wingman Randomizer by FalconLuma
Randomizes weapons and performance for all standard aircraft

-------------------------------------------------------------------------------------------------------------
Installation and Usage
-------------------------------------------------------------------------------------------------------------

1. Extract the contents of the .zip to your Project Wingman install folder (e.g. C:\Program Files (x86)\Steam\steamapps\common\Project Wingman)
2. Run PWRandomizer.exe
3. Choose your settings and press 'Run Randomizer' button
4. Run Project Sicario Merger (PSM)
5. Run Project Wingman

-------------------------------------------------------------------------------------------------------------
Main Settings
-------------------------------------------------------------------------------------------------------------

Randomizer Seed
  - Determines the output of the randomizer
    - Using the same seed with teh same settings will always produce the same result
  - You can enter litterally anything in the text box
  OR
  - Pressing 'Generate Random Seed' will create a random seed of a 20 digit long Integer
    - Using a generated seed will overwrite anything already in the text box
 
Attribute Randomizer Selection
  - Use the checkboxes to select what parts of the game to randomize
    - Plane Performance: Randomizes the performance stats of all planes (Speed, Roll Rate, etc.)
    - Plane Weapons: Randomizes the weapons avaliable to each plane
      - All planes retain the same number options avaliable per slot as in a unmodded game
    - Weapon Stats: Randomizes attributes for player weapons (Ammo, Reload, Range, etc.)
      - Due to game limitations attributes such as damage and explosion radius cannot be modified

Weapon Variations 
  - Defaults to 1
  - Defines how many different versions of each weapon shopuld be created
    - i.e. a value of 3 would cause 3 different versions of MLAA to randomized with different stats
    - I reccomend a value between between 1 and 3 
    - This setting has a large impact on how long it will take to run PSM 
    
-------------------------------------------------------------------------------------------------------------
Advanced Settings
-------------------------------------------------------------------------------------------------------------

THE 'SAVE SETTINGS' BUTTON MUST BE PRESSED AND 'SETTINGS SAVED' TEXT MUST APPEAR FOR CHANGES TO TAKE EFFECT

These setting allow you to fine tune the the output of the randomizer by controlling the ranges that stats 
can be assigned. 
  - Randomized stats will be >= min value and <= max value
  - By default all stat ranges are initiallised to ranges found naturally in the game
 

Aircraft Performance - These setting directly correlate the to the stats shown in the hangar
  - Response: Controls how long it takes for a input to be fully realised - higher is faster 
    - e.g. how long it takes to move the alierons from a nuetral position to the requested position
  - Speed: The top speed of the aircraft in km/h
  - Acceleration: How quickly the aircraft accelerates - higher is faster
  - Roll: How quickly the aircraft will roll - higher is faster
  - Turn: How tightly the aircraft will pitch - higher is faster
  - Yaw: How quickly the aircraft will yaw - higher is faster
  
Weapon Selection
  - All weapons wiht a checked box next to them will be included in the weapon pool for randomization
  - NOTE: EFUB (the nuke) is excluded by default but can be enabled
  - Unguided Chance: Sets the chance for a naturally unguided weapon to remain unguided
    - Decimal between 0 and 1
      - 0 = All unguided weapons will become guided
      - 1 = All unguided weapons will stay unguided
      - Any other values = any given unguioded weapon will become guided at the set probability
      - Any value outside this range will be rounded to either 0 or 1 whichever is closer
      
Weapon Attributes
  - Reload: time in seconds for how long it takes to reload a single hardpoint
  - Ammunition: The number of times a wepaon can be fired
  - Loaded: the max number of time a weapon can be fired before waiting for reload
    - e.g. unmodded ASM is 1, unmodded STDM is 2
    - if a weapon has value exceddig the number of equipped hardpoints this value equals the hardpoint count
  - Max Locks: The number of enemies that can be simulutaneously locked on to
    - In practice this is limited to equiped hardpoints * salvo size 
      - e.g. 2 MLAA-3 harpoints would be limited to 6 locks
  - Range: The max distance in meters that weapon can lock onto a enemy from
  
  The following stats are exclusive to the gun pods (RGP, MGP, HGP, CGP), the Railgun uses the stats above
  - Gun Reload: the time in seconds between shots of a single gunpod
  - Gun Ammo: The number of shots a single slot of a gunpod has.
