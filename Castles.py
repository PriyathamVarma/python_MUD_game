# This function (castle) gives the information of all castles depending upon the input given bu user.
# information is the argument passed through an input
def castle():
  
  castle_information = input("***  Enter names of any one of the castles(Warkworth, Trematon, Aylsham, Bodium, Conwy) ***:").upper()
  with open("game_play.txt", "a") as fileOpen:
    if castle_information == 'WARKWORTH':
      f = open("assets/castles/warkworth.txt","r")
      print(f.read())
      fileOpen.write(f'player entred info for WARKWORTH')
      print(f"Warkworth, Kingdom of great king aslan who looks after his subjects very well and rules with bravery and courage.\nHe is gifted with the most beautiful girl Diana, little princess of warkworth.\nWarkworth is so big and conatins great walls for its protection.")
    elif castle_information == 'TREMATON':
      f = open("assets/castles/trematon.txt","r")
      print(f.read())
      fileOpen.write(f'player entred info for TREMATON')
      print(f'Trematon, evil castle of the Evil Dragon Smaug. \nIt is dark, evil and so huge that no one can see the top of the castle except the dragon which can fly.')
    elif castle_information == 'AYLSHAM':
      f = open("assets/castles/aylsham.txt","r")
      print(f.read())
      fileOpen.write(f'player entred info for AYLSHAM')
      print(f'Aylsham, water kingdom conatining magical objects like flying shoes, flaring sword and magical rope. \nIt is wide and powerful with many magical creatures.')
    elif castle_information == 'BODIUM':
      f = open("assets/castles/bodium.txt","r")
      print(f.read())
      fileOpen.write(f'player entred info for BODIUM')
      print(f'Bodium, mighty kingdom of northern seas contains many magical objects like pridwen, the famous excalibar \nand galatine which have many poerful powers.')
    elif castle_information == 'CONWY':
      f = open("assets/castles/conwy.txt","r")
      print(f.read())
      fileOpen.write(f'player entred info for CONWY')
      print('Conwy, kingdom of great king varmadrof is wide and majestical. \nAHalo, Fail not that never fails its target, Talyn all have magical powers worth weilding.') 
    else:
      fileOpen.write(f'player entred wrong name for castle')
      print('\033[1;31m We told you to enter the name of castle among the given options. Unfortunately we are still in 1970s and can only develop games with minimum features')  
      castle()
    fileOpen.close()
    

  