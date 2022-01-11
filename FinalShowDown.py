from Castles_Weapons_Selection import *


class FinalShowDown(CharacterCreation):
  # Starting the game
  def __init__(self,name,kingdom,Strengths):
    super().__init__(name,kingdom,Strengths)

  def fight(self):
    winning_weapons_list = ['MAGIC ROPE','EXCALIBAR','HALO']
    """selected_weapons_list = [weapon_1_selected,weapon_2_selected,weapon_3_selected]"""
    global x
    x = 0
    for i in range(len(selected_weapons_list)):
      if selected_weapons_list[i] in winning_weapons_list:
        x+=1

      else:
        x-=1 

    print(x)
    # If statement to decide happy or sad ending
    if x == 3:
      print(f'{self.name}, Prince of {self.kingdom} used {selected_weapons_list[0]} to make the princess escape with the rope.\n While, the princess was escaping he used {selected_weapons_list[2]} to stop the dragon from confroanting as it emitted immense light that blinded the dragon\n. When the princess escaped and hided in a safe location {self.name} used {selected_weapons_list[1]} to pierce the dragons body and kill it') 
    else:
      print(f'{self.name}, Prince of {self.kingdom} lost the battle with the dragon and couldnt save the princess. Long Live Humanity. We lost the battle')
