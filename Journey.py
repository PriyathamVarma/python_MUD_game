from Play import Play
from Castles_Weapons_Selection import *
from FinalShowDown import FinalShowDown


def Game(name,country,Strengths):

  start_game = input("*** Press 'START' to start the play or 'EXIT' to exit the game: ***").upper()
  f = open("game_play.txt", "a")
  f.write(f'\n{name} started the game by entering {start_game}')
  f.close()

  # If the user starts the game with start
  if start_game == 'START':

    player_play = Play(name,country,Strengths) # goes to player class
    box_1_answers_selection(name,country,Strengths)# Iterations for other weapon selections are done here
    final_fight = FinalShowDown(name,country,Strengths)
    final_fight.fight()

  # If the user exits the game with exit
  elif start_game == 'EXIT':
    from new import new
    new()
  # If the user inputs other text 
  else:
    Game(name,country,Strengths) 
