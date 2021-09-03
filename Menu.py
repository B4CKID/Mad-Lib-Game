import time

from funcs import *
from Mad_Lib_Generator.Mad_Libs import MadLibs

class Menues:
  def menu():
    print("Welcome to Madlib and Sadlibs")
    time.sleep(5)
    clear()
    print('Please choose your Madlib Category')
    time.sleep(3)
    user_input = input( ' 1. Theme Park\n 2. Zoo Trip\n 3. Arcade Trip\n 4. First Day of School\n 5. To Exit Game\n ')
    clear()
    
    while user_input:
      if user_input == '1':
        MadLibs.mad_lib1()
        break

      elif user_input == '2':
        MadLibs.mad_lib2()
        break
      elif user_input == '3':
        MadLibs.mad_lib3()
        break
      elif user_input == '4':
        MadLibs.mad_lib4()
        break
      
      elif user_input == '5':
        print('Terminating program')
        break
    

      else: 
        print('Not a valid choice!')
        Menues.menu()
    
  def cont():# user wants to continue using game
    print('Would you like to play again? y/n: ')
    time.sleep(5)
    u2 = input('Enter y/n')
    if u2 == 'y':
      print("Lets play aganin!")
      time.sleep(3)
      Menues.menu()

    elif u2 == 'n':
      print("We'll see you next time!")
    else:
      print('Invalid Choice')
      time.sleep(3)
      Menues.cont()



  
