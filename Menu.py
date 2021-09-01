import time


from Mad_Lib_Generator.Mad_Libs import MadLibs


def menu():
  print("Welcome to Madlib and Sadlibs")
  time.sleep(5)
  print('Please choose your Madlib Category')
  time.sleep(3)
  user_input = input( ' 1. Theme Park\n 2. Zoo Trip\n 3. Arcade Trip\n 4. First Day of School ')

  while user_input != 'q':
    if user_input == '1':
      MadLibs.mad_lib1()

    elif user_input == '2':
      break
    elif user_input == '3':
      break 
    elif user_input == '4':
      break
    
    elif user_input == 'q':
      print('Terminating program')
  

    else: 
      print('Not a valid choice!')
      break

  menu()





  
