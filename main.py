# This is the main python file which starts the game
# IMPORTS

from Game import Game

def CharacterFeatures():
  global name,country,Strengths
  print('\033[1;35m ******** Create your prince character ********')
  name = input('*** Enter your name ***: ')
  country = input('*** Enter your kingdoms name ***: ')
  Strengths = input('*** Enter your strengths ***: ')

def start():

    CharacterFeatures()
    
    Game(name,country,Strengths)


# if the function is not imported
if __name__ == "__main__":
  start()
