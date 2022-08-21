# This is the main python file which starts the new game

def CharacterFeatures():
  global name,country,Strengths
  print('\033[1;35m ******** Create your prince charcter ********')
  name = input('*** Enter your name ***: ')
  country = input('*** Enter your country name ***: ')
  Strengths = input('*** Enter your strengths ***: ')

def new():
    try:
      # to avoid circular imports
        print("****** NEW GAME ******")
        from Game import Game
        f = open("game_play.txt", "a")
        CharacterFeatures()
        f.write(f"\nPlayer exited the game")
        f.write(f"\nNEW GAME STARTS for {name}, Prince of {country} who has {Strengths} as his strengths \n")
        f.close()
        Game(name,country,Strengths)
        
    except NameError:
        print("We already expected this error mate")    


