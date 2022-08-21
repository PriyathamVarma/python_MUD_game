""" Class for game play"""
# This class can be sued for controlling play options like attack, run or other functionalities
# Intended for future use

from CharacterCreation import CharacterCreation

class Play(CharacterCreation):
  # Starting the game
  def __init__(self,name,country,Strengths):
    
    print(f'\033[1;35m ​Diana, Princess of Warkworth, is a beautiful girl with such beauty which could be matched only by Aphrodite.\n She is sweet and lovely and is loved by everyone in the kingdom. Her father, King Aslan, is so much attached to her.\n One day when the princess is going to bed, an evil dragon, Smaug, attacked the kingdom and abducted her.\n The dragon took her to a dark castle, Tremato​n and locked her up. The dragon wants to kill the princess during the day of the blue moon, which gives the dragon powers to give life to other dragons.\n If this happens then, that will be the end of humanity. To get her daughter back and save the world, King Aslan chooses princes from various kingdoms.\n The task of the princes is to collect a few magical objects that will be useful in fighting the dragon. They have to save the princess and slay the dragon.\n But, the princes need to be very careful as they pass each checkpoint and collect each magical object.\n Because only the right combination of magical things can save the princess and fight the dragon, even one mistake in selecting the items will prove to be of no use in battle against the dragon. ')
    super().__init__(name,country,Strengths) # Character creation class gets initiated

    f = open("game_play.txt", "a")
    f.write(f'\n*****************STORY LINE **************\n ​Diana, Princess of Warkworth, is a beautiful girl with such beauty which could be matched only by Aphrodite.\n She is sweet and lovely and is loved by everyone in the kingdom. Her father, King Aslan, is so much attached to her.\n One day when the princess is going to bed, an evil dragon, Smaug, attacked the kingdom and abducted her.\n The dragon took her to a dark castle, Tremato​n and locked her up. The dragon wants to kill the princess during the day of the blue moon, which gives the dragon powers to give life to other dragons.\n If this happens then, that will be the end of humanity. To get her daughter back and save the world, King Aslan chooses princes from various kingdoms.\n The task of the princes is to collect a few magical objects that will be useful in fighting the dragon. They have to save the princess and slay the dragon.\n But, the princes need to be very careful as they pass each checkpoint and collect each magical object.\n Because only the right combination of magical things can save the princess and fight the dragon, even one mistake in selecting the items will prove to be of no use in battle against the dragon. \n******************************')
    f.close()


