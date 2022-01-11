""" Characters Creation with characters features"""

# This class can be used for characters creation and modifications
# Intended for future use

class CharacterCreation:

  def __init__(self,name,kingdom,Strengths):
    self.name = name
    self.kingdom = kingdom
    self.Strengths = Strengths 
    f = open("game_play.txt",'a')
    f.write(f'\n Player Name:{name} \nKingdom:{kingdom} \n Strengths:{Strengths} \n')
    f.close()
    print(f'\033[1;32m *** {self.name.upper()}, prince of the legendary kingdom of {self.kingdom.upper()} who have {self.Strengths} has started his journey to save Diana and kill the evil dragon, Smaug and save humanity from extinction ***')



