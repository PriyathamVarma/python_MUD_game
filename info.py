""" This file conatins info function which acts like a pivot function for getting
information about castles or objects or charcters """
# Imports
from Castles import castle
from Objects import objects
from Characters import characters

def info():
    
    information = input(f'\033[1;31m Enter "OBJECTS" for object information.\nEnter "CASTLES" for castles information. \nEnter "CHARCATERS" for characters information: ').upper()
    with open("game_play.txt",'a') as fileOpen:
        if information == 'CASTLES':
            castle()
            fileOpen.write("Player entered castle to look at the information")
        elif information == 'OBJECTS':
            objects()
            fileOpen.write("Player entered objects to look at the information")  
        elif information == 'CHARACTERS':
            characters()
            fileOpen.write("Player entered characters to look at the information")
        else:
            print("Please re-enter correctly mate. We already told you this is a very old MUD game not your regular FORTNITE game")
            fileOpen.write(f"\nPlayer entered {information} to look at the information and got renter message\n")
            info()
            


