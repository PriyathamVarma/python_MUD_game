""" Class for game play"""
# This class can be sued for controlling play options like attack, run or other functionalities
# Intended for future use

from CharacterCreation import CharacterCreation

class Play(CharacterCreation):
  # Starting the game
  def __init__(self,name,country,Strengths):
    
    print(f'The amazing adventurer,{name} from {country} with {Strengths} has started his journey to find the city of El Dorado. He have to find two missing symbols in order to get to the place. The first one is about an animal which is so ferocious and second one is a flying god.')
    super().__init__(name,country,Strengths) # Character creation class gets initiated



