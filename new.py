# This is the main python file which starts the new game

def CharacterFeatures():
  global name,kingdom,Strengths
  print('\033[1;35m ******** Create your prince charcter ********')
  name = input('*** Enter your name ***: ')
  kingdom = input('*** Enter your kingdoms name ***: ')
  Strengths = input('*** Enter your strengths ***: ')

def new():
    try:
      # to avoid circular imports
        from Game import Game
        f = open("game_play.txt", "a")
        CharacterFeatures()
        f.write(f"\nPlayer exited the game")
        f.write(f"\nNEW GAME STARTS for {name}, Prince of {kingdom} who has {Strengths} as his strengths \n")
        f.close()
        selected_weapons_list = []
        Game(name,kingdom,Strengths)
        
    except NameError:
        print("We already expected this error mate")    


