"""# Characters description"""

def characters():
  characters_information = input('*** Enter names of any one of the characters(Aslan, Diana, Smaug) ***:').upper()
  if characters_information == 'ASLAN':
    print('\033[1;35m Aslan, King of Warkworth and father of Diana. Furious, empathetic and powerful')
  elif characters_information == 'DIANA':
    print('\033[1;35m Diana, beautiful princess of warkworth kingdom. Calm, beautiful and cheerful girl.')
  elif characters_information == 'SMAUG':
    print('\033[1;35m Smaug, malifiecient dragon who wants to kill all humanity and rule the world with dragons.\n **** STRENGHTS ****: Capable of emitting fire from all sides, Can smell all living beings,Can withstand extreme weather conditions, can fly to any height and swim into any depth.\n **** WEAKNESS **** : Light, Music and Rats')
  else:
    print('\033[1;31m We told you to enter the name of the character among the given options. Unfortunately we are still in 1970s and can only develop games with minimum features')
    characters()