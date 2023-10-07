Project Wingman Randomizer by FalconLuma

-------------------------------------------------------------------------------------------------------------
Distribution Sources
-------------------------------------------------------------------------------------------------------------
https://www.nexusmods.com/projectwingman/mods/355 - Stable version, not updated regularly
https://github.com/FalconLuma/Project-Wingman-Randomizer - Likely to be more up-to-date than Nexus, both
                                                           stable and experimental builds

-------------------------------------------------------------------------------------------------------------
Compatibility
-------------------------------------------------------------------------------------------------------------

Requires Project Sicario Merger by agc93
  - https://www.nexusmods.com/projectwingman/mods/270
  - https://github.com/agc93/project-sicario

The randomizer mod will conflict with any mods that alter the performance or armament of aircraft or weapons
  - e.g. Balanced Wingman, All Weapons for All PLanes, etc.
  - There should be no conflicts with purely aesthetic mods: skins, model-swaps, audio replacement, etc.
  - If used alongside a model-swap with custom loadouts make sure the randomizer is the last mod
    alphabetically to avoid the randomizer mod being overwritten e.g. add a 'z' to the start of the filename

-------------------------------------------------------------------------------------------------------------
Installation and Usage
-------------------------------------------------------------------------------------------------------------

1. Extract the contents of the .zip to your Project Wingman install folder
  - e.g. C:\Program Files (x86)\Steam\steamapps\common\Project Wingman
2. Run PWRandomizer.exe
3. Choose your settings and press 'Run Randomizer' button
4. Run Project Sicario Merger (PSM) adn wait for it to finish
5. Run Project Wingman

-------------------------------------------------------------------------------------------------------------
Main Settings
-------------------------------------------------------------------------------------------------------------

Randomizer Seed
  - Determines the output of the randomizer
    - Using the same seed with the same settings will always produce the same result
  - You can enter literally anything in the text box
  OR
  - Pressing 'Generate Random Seed' will create a random seed of a 20 digit long integer
    - Using a generated seed will overwrite anything already in the text box
    - Once a seed is generated both the textbox and button are disabled to ensure repeatability
 
Attribute Randomizer Selection
  - Use the checkboxes to select what parts of the game to randomize
    - Unreleased Planes: Will add six unreleased planes that are in a near-complete state
      - FC.2M, G-10, X-16Z. F/F-18, Sk.30, F/T-15
      - For non-randomized unlocks, aircraft are unlocked in positions based on their un-modded performance
    - Plane Performance: Randomizes the performance stats of all planes (Speed, Roll Rate, etc.)
    - Plane Weapons: Randomizes the weapons available to each plane
    - Weapon Stats: Randomizes attributes for player weapons (Ammo, Reload, Range, etc.)
      - Due to game limitations, attributes such as damage and explosion radius cannot be modified
      - When using this option the normal weapon descriptions will be replaced with the new weapon stats
    - Options/Slot: Randomizes how many weapon options are available for every weapon slot on every plane
      - If left unchecked all slots will have the same number of options as in an unmodified game
      - Any slots that normally have 0 options will not change
    - Mission Order: Randomizes the order of missions
      - Does not affect the order of missions in the Free Mission menu however the menu names will be changed
      - NOTE: Black Flag will always be the first mission of the campaign for reasons outside my control
    - Unlock Order: Select the order in which you want he aircraft to unlock
      - Normal: Aircraft will unlock based on how far into the campaign you are
        - i.e. No matter what mission is 2nd the SV-37 will be unlocked upon completion
        - Provides a smoother experience when enabled as your more likely to get a better plane earlier
      - Mission: Aircraft will unlock after completing the mission that usually unlocks them
        - i.e. Frontiers will always unlock the SV-37 even if it's the last mission in the campaign
        - Can cause you to be stuck with a starter aircraft for a long time depending on RNG
      - Random: Aircraft unlocks are shuffled throughout all 21 missions
        - No mission can unlock more than 2 aircraft upon completion
    - Balanced Wingman Compatibility: Adds the weapons from the Balanced Wingman mod to the weapon pool
      - Requires Balanced Wingman is installed and above the randomizer in load order (should be by default)
Weapon Variations 
  - Defaults to 1
  - Defines how many versions of each weapon should be created
    - i.e. a value of 3 would cause 3 different versions of MLAA to randomized with different stats
    - This setting has a large impact on how long it will take to run PSM
    - A value between 1 and 3 is recommended

-------------------------------------------------------------------------------------------------------------
Advanced Settings
-------------------------------------------------------------------------------------------------------------

!THE 'SAVE SETTINGS' BUTTON MUST BE PRESSED AND 'SETTINGS SAVED' TEXT MUST APPEAR FOR CHANGES TO TAKE EFFECT!

These setting allow you to fine tune the output of the randomizer by controlling the ranges that stats
can be assigned. 
  - Randomized stats will be >= min value and <= max value
  - By default all stat ranges are initialized to the ranges found naturally in the game

Aircraft Performance - These settings directly correlate to the stats shown in the hangar
  - Response: Controls how long it takes for an input to be fully realised - higher is faster
    - e.g. how long it takes to move the ailerons from a neutral position to the requested position
    - Also affects the camera lag when manoeuvring
    - This is an arbitrary unit
  - Speed: The top speed of the aircraft in km/h
  - Acceleration: How quickly the aircraft accelerates - higher is faster
  - Roll: How quickly the aircraft will roll - higher is faster
  - Turn: How tightly the aircraft will pitch - higher is faster
  - Yaw: How quickly the aircraft will yaw - higher is faster
  
Weapon Selection
  - All weapons with a checked box next to them will be included in the weapon pool for randomization
    - NOTE: EUFB (the nuke) is NOT selected by default, but can be enabled
    - Weapons that are not available in the base game, but are in files and work properly are included here
  - Unguided Chance: Sets the chance for a naturally unguided weapon to remain unguided
    - Decimal between 0 and 1
      - 0 = All unguided weapons will become guided
      - 1 = All unguided weapons will stay unguided
      - Any values in this range = probability at which each unguided weapon will stay unguided
      - Any value outside this range will be rounded to either 0 or 1 whichever is closer
  - Options per Slot: The min and max number of weapons that will available for each weapon slot
      
Weapon Attributes
  - Reload: time in seconds for how long it takes to reload a single hardpoint
  - Ammunition: The number of times a weapon can be fired
  - Loaded: the max number of time a weapon can be fired before waiting for reload
    - e.g. un-modded ASM is 1, un-modded STDM is 2
    - if a weapon has value exceeding the number of equipped hardpoints this value equals the hardpoint count
  - Max Locks: The number of enemies that can be simultaneously locked on to
    - In practice this is limited to equipped hardpoints * salvo size
      - e.g. 2 MLAA-3 hardpoints would be limited to 6 locks
  - Range: The max distance in meters that weapon can lock onto an enemy from
  
  The following stats are exclusive to the gun pods (RGP, MGP, HGP, CGP), the Railgun uses the stats above
  - Gun Reload: the time in seconds between shots for a single gunpod
  - Gun Ammo: The number of shots a single slot of a gunpod has.
