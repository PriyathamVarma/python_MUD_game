from Play import Play
from Castles_Weapons_Selection import *
from FinalShowDown import FinalShowDown


def Game(name,kingdom,Strengths):

  start_game = input("*** Press 'START' to start the play or 'EXIT' to exit the game: ***").upper()
  f = open("game_play.txt", "a")
  f.write(f'\n{name} started the game by entering {start_game}')
  f.close()

  # If the user starts the game with start
  if start_game == 'START':

    player_play = Play(name,kingdom,Strengths) # goes to player class
    f = open("game_play.txt", "a")
    castle_1_weapon_selection(name,kingdom,Strengths)# Iterations for other weapon selections are done here
    print(f'\033[1;32m {name.upper()} selected {selected_weapons_list[0]} at Aylsham, {selected_weapons_list[1]} at Bodium and {selected_weapons_list[2]} at Conwy to slay the dragon and save the Princess')
 
    final_fight = FinalShowDown(name,kingdom,Strengths)
    final_fight.fight()
    f.close()


  # If the user exits the game with exit
  elif start_game == 'EXIT':
    from new import new
    """print(f'\033[1;32m **** {name} exited the game ****')"""
    f = open("game_play.txt", "a")
    f.write(f'\n **** {name} exited the game **** \n')
    f.close()
    new()
  # If the user inputs other text 
  else:
    print('\033[1;31m Please press START and nothing else. Remember we are still in infancy stage and this is not a high end game :) :) :)')
    f = open("game_play.txt", "a")
    f.write('\{name} got a message as Please press START and nothing else. Remember we are still in infancy stage and this is not a high end game :) :) :)')
    f.close()
    Game(name,kingdom,Strengths) 
