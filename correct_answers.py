
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
    answer_1_selected = input('The big cat that is ferocious and native to the country:').upper()
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
      box_1_answers_selection(name,country,Strengths)


def box_2_answers_selection(name,kingdom,Strengths):
    answer_2_selected = input('The flying god of ancient mayans:').upper()
    if answer_2_selected in box_2_answers_list :
      print(f'{name} selected {answer_2_selected}') 
      selected_answers_list.append(answer_2_selected)
        
    elif answer_2_selected == 'INFO':
      info()
      box_2_answers_selection(name,kingdom,Strengths) 
    elif answer_2_selected == 'EXIT':
      print("Player exited the game")
      new() 
    else:
      box_2_answers_selection(name,kingdom,Strengths)


  