
from Castles import *
from Objects import *
from Play import *
from Journey import *
from info import info
from new import new

box_1_answers_list = ['LEOPARD' , 'TIGER' , 'JAGUAR']
box_2_answers_list = ['EAGLE' , 'VULTURE' , 'KITE']


global selected_answers_list,answers_1_selected,answers_2_selected
selected_answers_list = []

def box_1_answers_selection(name,country,Strengths): 
    answer_1_selected = input('The big cat that is ferocious').upper()
      # if condition for selecting weapon in castle 1
    if answer_1_selected in box_1_answers_list:
      print(f'{name} selected {answer_1_selected}') 
      selected_answers_list.append(answer_1_selected)
      box_2_answers_selection(name,country,Strengths)
    elif answer_1_selected == 'INFO':
      info()  
      box_1_answers_selection(name,country,Strengths)
    elif answer_1_selected == 'EXIT':
      print("Player exited the game")
      new()     
    else:
      print(f'\033[1;31m Enter the name correctly, hurry up the princess is in danger {name}, Prince of {country}')  
      box_1_answers_selection(name,country,Strengths)


def box_2_answers_selection(name,kingdom,Strengths):
    weapon_2_selected = input('*** Select any weapon(PRIDWEN or EXCALIBAR or GALATINE)from Bodium that you want to fight with the dragon (HINT: Enter info or EXIT) ***:').upper()
    if weapon_2_selected in box_2_answers_list :
      print(f'\033[1;32m {name} selected {weapon_2_selected} at BODIUM') 
      selected_answers_list.append(weapon_2_selected)
        
    elif weapon_2_selected == 'INFO':
      info()
      box_2_answers_selection(name,kingdom,Strengths) 
    elif weapon_2_selected == 'EXIT':
      print("Player exited the game")
      new() 
    else:
      box_2_answers_selection(name,kingdom,Strengths)


  