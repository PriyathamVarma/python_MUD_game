# This file conatins all information about all functions, variables, classes and methods
# Also, this file explains about the code in detail step wise.


# Step 1
The main.py file is executed first which conatins start() function that initiates CharacterFeatures() function.
CharacterFeatures() function contains three arguments name,kingdom and strengths of the character.
Then the game starts with Game() function containing three arguements - name, kingdom and strengths from the character CharacterFeatures

#Step 2
Game.py file contains a input which redirects to start if user enters start or exits the game and redirects to exit
if entered exit or throws an re enter message and restarts Game() function if wrong input is given

#Step3
The Game() functions initiates Play() class which takes the properties from CharacterCreation class. Then
it initiates castle_1_weapon_selection() function.

#Step4
castle_1_weapon_selection() function along with three arguments saves the selected weapon at castle 1 
in a list called selected_weapons_list then redirects to castle 2 which the redirects to castle 3 collecting wepaons along the way.

#Step5
Finally, the showdon is started with FinalShowDown class that takes properties from 
CharacterCreation class and uses it for outputting the results.

#Important Notes
1. At all chaeckpoints the progress is saved in game_paly.txt
2. At all check points exit is given which redirects to new() function in new.py which restarts the game
3. assets folders contains characters, objects and castles text pictures  in ascii code
4. The description of castles can be found at castles.py
5. The description of objects can be found at objects.py
6. The description of characters can be found at characters.py

# Test cases:
1. All function test cases can be found at main_test.py(To test enter python -m unittest main_test.py)
1. Game test cases can be found at main_test.py(To test enter python -m unittest game_test.py)
1. Play test cases can be found at main_test.py(To test enter python -m unittest play_test.py)
