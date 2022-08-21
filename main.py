# The file to start the journey

from Journey import Game

def traits():
  global name,country,Strengths
  name = input('Name : ')
  country = input('Country : ')
  Strengths = input('Strengths : ')

def start():

    traits()   
    Game(name,country,Strengths)


# if the function is not imported
if __name__ == "__main__":
  start()
