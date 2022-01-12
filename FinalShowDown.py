""" This file contains FinalShowDown class which conatins fight method"""
from Castles_Weapons_Selection import *



class FinalShowDown(CharacterCreation):
  # Starting the game
  def __init__(self,name,kingdom,Strengths):
    super().__init__(name,kingdom,Strengths)
    global x


  def fight(self):
    winning_weapons_list = ['MAGIC ROPE','EXCALIBAR','HALO']
    
    x = 0
    print(f"x value for checking:{x}")
    from Castles_Weapons_Selection import selected_weapons_list
    selected_weapons_list =  list(set(selected_weapons_list))
    for i in range(len(selected_weapons_list)):
      if selected_weapons_list[i] in winning_weapons_list:
        x+=1
        print(x)

    with open("game_play.txt","a") as fileOpen:
      print(f"\n Player scored {x} (Player needs 3 to win)\n")
      # If statement to decide happy or sad ending
      if x == 3:
        print(f'{self.name}, Prince of {self.kingdom} used the MAGIC ROPE to make the princess escape with the rope.\n While, the princess was escaping he used HALO to stop the dragon from confroanting as it emitted immense light that blinded the dragon\n. When the princess escaped and hided in a safe location {self.name} used EXCALIBAR to pierce the dragons body and kill it') 
        print(f"\nHAPPY ENDING\n")
        fileOpen.write(f"\n{self.name}, Prince of {self.kingdom} used {selected_weapons_list[0]} to make the princess escape with the rope.\n While, the princess was escaping he used {selected_weapons_list[2]} to stop the dragon from confroanting as it emitted immense light that blinded the dragon\n. When the princess escaped and hided in a safe location {self.name} used {selected_weapons_list[1]} to pierce the dragons body and kill it")
        fileOpen.write(f"\nHAPPY ENDING\n")
      elif x!=3:
        print(f'{self.name}, Prince of {self.kingdom} lost the battle with the dragon and couldnt save the princess. Long Live Humanity. We lost the battle')
        print(f"\SAD ENDING\n")
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
