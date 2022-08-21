# This is the main python file which starts the new game

def CharacterFeatures():
  global name,country,Strengths
  print('\033[1;35m ******** Create Character ********')
  name = input('*** Enter your name ***: ')
  country = input('*** Enter your country name ***: ')
  Strengths = input('*** Enter your strengths ***: ')

def new():
    try:
      # to avoid circular imports
        print("****** NEW GAME ******")
        from Journey import Game
        CharacterFeatures()
        Game(name,country,Strengths)
        
    except NameError:
        print("We already expected this error mate")    


