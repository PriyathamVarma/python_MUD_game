""" This file contains FinalShowDown class which conatins fight method"""

from Castles_Weapons_Selection import *

class FinalShowDown(CharacterCreation):
  # Starting the game
  def __init__(self,name,kingdom,Strengths):
    super().__init__(name,kingdom,Strengths)

  def fight(self):
    winning_weapons_list = ['MAGIC ROPE','EXCALIBAR','HALO']
    global x
    x = 0
    from Castles_Weapons_Selection import selected_weapons_list
    selected_weapons_list =  list(set(selected_weapons_list))
    for i in range(len(selected_weapons_list)):
      k = 0
      if selected_weapons_list[i] in winning_weapons_list:
        k+=1

      else:
        k-=1

    with open("game_play.txt","a") as fileOpen:
      print(f"\n Player scored {x} (Player needs 3 for winning the game)\n")
      fileOpen.write(f"\nFINAL SHOWDOWN STARTS\n")
      fileOpen.write(f'\n{self.name.upper()} selected {selected_weapons_list[0]} at Aylsham, {selected_weapons_list[1]} at Bodium and {selected_weapons_list[2]} at Conwy to slay the dragon and save the Princess')
      fileOpen.write(f" Player scored {x} (Player needs 3 for winning the game)")
      # If statement to decide happy or sad ending
      if k == 1:
        print(f'{self.name}, Prince of {self.kingdom} used {selected_weapons_list[0]} to make the princess escape with the rope.\n While, the princess was escaping he used {selected_weapons_list[2]} to stop the dragon from confroanting as it emitted immense light that blinded the dragon\n. When the princess escaped and hided in a safe location {self.name} used {selected_weapons_list[1]} to pierce the dragons body and kill it') 
        print(f"\nHAPPY ENDING\n")
        fileOpen.write(f"\n{self.name}, Prince of {self.kingdom} used {selected_weapons_list[0]} to make the princess escape with the rope.\n While, the princess was escaping he used {selected_weapons_list[2]} to stop the dragon from confroanting as it emitted immense light that blinded the dragon\n. When the princess escaped and hided in a safe location {self.name} used {selected_weapons_list[1]} to pierce the dragons body and kill it")
        fileOpen.write(f"\nHAPPY ENDING\n")
      else:
        print(f'{self.name}, Prince of {self.kingdom} lost the battle with the dragon and couldnt save the princess. Long Live Humanity. We lost the battle')
        print(f"\SAD ENDING\n")
        fileOpen.write(f'\n{self.name}, Prince of {self.kingdom} lost the battle with the dragon and couldnt save the princess. Long Live Humanity. We lost the battle')
        fileOpen.write(f"\nSAD ENDING\n")
        restart_game = input(f'Do you want to restart the game?(PRESS Y for restart or any button to exit):').upper()
        if restart_game == "Y":
          from Castles_Weapons_Selection import selected_weapons_list          
          selected_weapons_list = []
          print(selected_weapons_list)

          from new import new
          new()
        else:
          try:
            print("GAME OVER")
          except AssertionError:
            print("Assertion error found")  
      fileOpen.close()  
