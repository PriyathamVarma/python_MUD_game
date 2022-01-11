"""# castle 1,2,3 weapon selection"""
from Castles import *
from Objects import *
from Play import *
from Game import *

castle_1_weapons_list = ['FLYING SHOES' , 'FLARING SWORD' , 'MAGIC ROPE']
castle_2_weapons_list = ['PRIDWEN' , 'EXCALIBAR' , 'GALATINE']
castle_3_weapons_list = ['HALO' , 'FAIL NOT' , 'TALYN HARP']

global selected_weapons_list,weapon_1_selected,weapon_2_selected,weapon_3_selected
selected_weapons_list = []

def castle_1_weapon_selection(name,kingdom,Strengths):
  weapon_1_selected = input('*** Select any weapon(Flying Shoes or Flaring Sword or Magic Rope) from Aylsham that you want to fight with the dragon (HINT: Enter info for weapons info) ***:').upper()
  # if condition for selecting weapon in castle 1
  if weapon_1_selected in castle_1_weapons_list:
    print(f'\033[1;32m {name} selected {weapon_1_selected} at AYLSHAM') 
    selected_weapons_list.append(weapon_1_selected)
    castle_2_weapon_selection(name,kingdom,Strengths)
  elif weapon_1_selected == 'INFO':
    objects()  
    castle_1_weapon_selection(name,kingdom,Strengths)
  else:
    print(f'\033[1;31m Enter the name correctly, hurry up the princess is in danger {name}, Prince of {kingdom}')  
    castle_1_weapon_selection(name,kingdom,Strengths)

def castle_2_weapon_selection(name,kingdom,Strengths):
  weapon_2_selected = input('*** Select any weapon(PRIDWEN or EXCALIBAR or GALATINE)from Bodium that you want to fight with the dragon (HINT: Enter info for weapons info) ***:').upper()
  # if condition for selecting weapon in castle 1
  if weapon_2_selected in castle_2_weapons_list :
    print(f'\033[1;32m {name} selected {weapon_2_selected} at AYLSHAM') 
    selected_weapons_list.append(weapon_2_selected)
    castle_3_weapon_selection(name,kingdom,Strengths)
  elif weapon_2_selected == 'INFO':
    objects()
    castle_2_weapon_selection(name,kingdom,Strengths)  
  else:
    print(f'\033[1;31m Enter the name correctly, hurry up the princess is in danger {name}, Prince of {kingdom}') 
    castle_2_weapon_selection(name,kingdom,Strengths)

def castle_3_weapon_selection(name,kingdom,Strengths):
  weapon_3_selected = input('Select any weapon(HALO or FAIL NOT or TALYN HARP)from CONWY that you want to fight with the dragon (HINT: Enter info for weapons info):').upper()
  # if condition for selecting weapon in castle 1
  if weapon_3_selected in castle_3_weapons_list :
    print(f'\033[1;32m {name} selected {weapon_3_selected} at AYLSHAM')
    selected_weapons_list.append(weapon_3_selected) 
  elif weapon_3_selected == 'INFO':
    objects()
    castle_3_weapon_selection(name,kingdom,Strengths)  
  else:
    print(f'\033[1;31m Enter the name correctly, hurry up the princess is in danger {name}, Prince of {kingdom}') 
    castle_3_weapon_selection(name,kingdom,Strengths)


  