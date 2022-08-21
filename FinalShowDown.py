""" This file contains FinalShowDown class which conatins fight method"""
from correct_answers import *

class FinalShowDown(CharacterCreation):
  # Starting the game
  def __init__(self,name,country,Strengths):
    super().__init__(name,country,Strengths)
    global x


  def fight(self):
    correct_answers_list = ['JAGUAR','EAGLE']
    
    x = 0
    print(f"x value for checking:{x}")
    from correct_answers import selected_answers_list
    selected_answers_list =  list(set(selected_answers_list))
    for i in range(len(selected_answers_list)):
      if selected_answers_list[i] in correct_answers_list:
        x+=1
        print(x)

      print(f"\n Player scored {x} (Player needs 2 to win)\n")
      # If statement to decide happy or sad ending
      if x == 2:
        print(f"\nThe city is found\n")

      elif x!=2:
        
        print(f"\The city is not found\n")
        restart_game = input(f'Do you want to restart the game?(PRESS Y for restart or any button to exit):').upper()
        if restart_game == "Y":
          from correct_answers import selected_answers_list          
          selected_answers_list = []
          print(selected_answers_list)

          from new import new
          new()
        else:
          try:
            print("JOurney Ends")
          except AssertionError:
            print("Assertion error found")  
      
