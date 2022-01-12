"""This file contains charcaters function which gives information about characters"""

def characters():
  characters_information = input('*** Enter names of any one of the characters(Aslan, Diana, Smaug) ***:').upper()
  with open("game_play.txt","a") as fileOpen:
    if characters_information == 'ASLAN':
      fileOpen.write(f"Player enetred {characters_information} for getting information")
      print('\033[1;35m Aslan, King of Warkworth and father of Diana. Furious, empathetic and powerful')
    elif characters_information == 'DIANA':
      fileOpen.write(f"Player enetred {characters_information} for getting information")
      print('\033[1;35m Diana, beautiful princess of warkworth kingdom. Calm, beautiful and cheerful girl.')
    elif characters_information == 'SMAUG':
      f = open("assets/characters/smaug.txt","r")
      print(f.read())
      fileOpen.write(f"Player enetred {characters_information} for getting information")
      print('\033[1;35m Smaug, malifiecient dragon who wants to kill all humanity and rule the world with dragons.\n **** STRENGHTS ****: Capable of emitting fire from all sides, Can smell all living beings,Can withstand extreme weather conditions, can fly to any height and swim into any depth.\n **** WEAKNESS **** : Light, Music and Rats')
    else:
      fileOpen.write(f"Player enetred {characters_information} for getting information and got a retry message")
      print('\033[1;31m We told you to enter the name of the character among the given options. Unfortunately we are still in 1970s and can only develop games with minimum features')
      characters()
    fileOpen.close()  