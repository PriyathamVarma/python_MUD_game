""" This file conatins objects function which gives the information of objects"""

def objects():
  object_information = input("*** Enter names of any one of the objects(FLYING SHOES, FLARING SWORD, MAGIC ROPE, PRIDWEN, EXCALIBAR,GALATINE, HALO,FAIL NOT, TALYN HARP) ***:").upper()
  with open("game_play.txt","a") as fileOpen:

    if object_information == 'FLYING SHOES':
      fileOpen.write(f"\n Player entered {object_information} for the information")
      print("Flying Shoes, magical shoes which gives the bearer the ability to fly")

    elif object_information == 'FLARING SWORD':
      fileOpen.write(f"\n Player entered {object_information} for the information")
      print('Flaring Sword, furious weapon that can emit fire.')

    elif object_information == 'MAGIC ROPE':
      fileOpen.write(f"\n Player entered {object_information} for the information")
      print('Magic Rope, a mysterious object that can work according to the bearers mind.')

    elif object_information == 'PRIDWEN':
      fileOpen.write(f"\n Player entered {object_information} for the information")
      print('Pridwen, solid armour that gives the weilder the power of invisibility.')

    elif object_information ==  'EXCALIBAR':
      fileOpen.write(f"\n Player entered {object_information} for the information")
      print('Excalibar, sword of mass destruction that can pierce through any object.')   

    elif object_information ==  'GALATINE':
      fileOpen.write(f"\n Player entered {object_information} for the information")
      print('Galatine, sword of power that can create ice and control ice.') 

    elif object_information ==  'HALO':
      fileOpen.write(f"\n Player entered {object_information} for the information")
      print('Halo, ring of light which can emit immense intensity of light.')   

    elif object_information ==  'FAIL NOT':
      fileOpen.write(f"\n Player entered {object_information} for the information")
      print('Fail not, a magical bow and arrow pair that never misses its target.') 

    elif object_information ==  'TALYN HARP':
      fileOpen.write(f"\n Player entered {object_information} for the information")
      print('Talyn Harp, a magic musical instrument which bewilders the opponents when the music is played.')    

    else:
      fileOpen.write(f"\n Player entered {object_information} for the information and got a message to renter")
      print('\033[1;31m We told you to enter the name of object among the given options. Unfortunately we are still in 1970s and can only develop games with minimum features') 
      objects() 

    fileOpen.close()       