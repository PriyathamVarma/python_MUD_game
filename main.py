# This is the main python file which starts the game
# IMPORTS

from typing import ValuesView
from Game import Game

def CharacterFeatures():
  global name,kingdom,Strengths
  print('\033[1;35m ******** Create your prince charcter ********')
  name = input('*** Enter your name ***: ')
  kingdom = input('*** Enter your kingdoms name ***: ')
  Strengths = input('*** Enter your strengths ***: ')

def start():
    f = open("game_play.txt", "w")
    CharacterFeatures()
    f.write(f"GAME STARTS for {name}, Prince of {kingdom} who has {Strengths} as his strengths")
    f.close()
    Game(name,kingdom,Strengths)


# if the function is not imported
if __name__ == "__main__":
  start()
