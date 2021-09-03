import time

from funcs import *
from Mad_Lib_Storage.Madlib_Text import Mads


class MadLibs:

  def __init__(self):
    return None

  def __repr__(self):
    return None
    
  def mad_lib1():
    first = input("Enter first word(This is should be an adjective): ")
    second = input("Enter second word (This is should be a plural nonun): ")
    third = input("Enter Third word (This is should be a noun): ")
    fourth = input("Enter Fouth word (This is should be an adverb): ")
    fifth = input("Enter Fifth word (This is should be a number): ")
    sixth = input("Enter sixth word This is should be an past tense verb): ")
    seventh = input("Enter seventh word (This is should be an -est adjective): ")
    eighth = input("Enter eighth word (This is should be an past tense verb): ")
    ninth = input("Enter ninth word (This is should be an adverb): ")
    tenth = input("Enter tenth word (This is should be an adjective): ")
    time.sleep(3)
    clear()
    for libs in Mads.mlb1:# Maybe use if statements
      new_libs = libs.replace("1", first)
      new_libs = new_libs.replace("2",second)
      new_libs = new_libs.replace ("3", third)
      new_libs = new_libs.replace ("4", fourth)
      new_libs = new_libs.replace ("5", fifth)
      new_libs = new_libs.replace ("6", sixth)
      new_libs = new_libs.replace ("7", seventh)
      new_libs = new_libs.replace ("8", eighth)
      new_libs = new_libs.replace ("9", ninth)
      new_libs = new_libs.replace ("*", tenth)
      print(new_libs)
    
  def mad_lib2():
    first = input("Enter first word(This is should be an adjective): ")
    second = input("Enter second word (This is should be a noun): ")
    third = input("Enter Third word (This is should be a past tense verb): ")
    fourth = input("Enter Fouth word (This is should be an adverb): ")
    fifth = input("Enter Fifth word (This is should be a adjective): ")
    sixth = input("Enter sixth word This is should be an noun): ")
    seventh = input("Enter seventh word (This is should be an noun): ")
    eighth = input("Enter eighth word (This is should be an adjective:) ")
    ninth = input("Enter ninth word (This is should be an verb): ")
    tenth = input("Enter tenth word (This is should be an adverb): ")
    eleventh = input("Enter tenth word (This is should be an past tense verb): ")
    twelth = input("Enter tenth word (This is should be an adjective): ")
    time.sleep(3)
    clear()
    for libs in Mads.mlb2:# Maybe use if statements
      new_libs = libs.replace("1", first)
      new_libs = new_libs.replace("2",second)
      new_libs = new_libs.replace ("3", third)
      new_libs = new_libs.replace ("4", fourth)
      new_libs = new_libs.replace ("5", fifth)
      new_libs = new_libs.replace ("6", sixth)
      new_libs = new_libs.replace ("7", seventh)
      new_libs = new_libs.replace ("8", eighth)
      new_libs = new_libs.replace ("9", ninth)
      new_libs = new_libs.replace ("*", tenth)
      new_libs = new_libs.replace ("&", eleventh)
      new_libs = new_libs.replace ("^", twelth)
      print(new_libs)

  def mad_lib3():
    first = input("Enter first word(This is should be an plural noun): ")
    second = input("Enter second word (This is should be a plural nonun): ")
    third = input("Enter Third word (This is should be a verb): ")
    fourth = input("Enter Fouth word (This is should be an noun): ")
    fifth = input("Enter Fifth word (This is should be a -ing verb): ")
    sixth = input("Enter sixth word This is should be an plural noun): ")
    seventh = input("Enter seventh word (This is should be a noun): ")
    eighth = input("Enter eighth word (This is should be an plural noun): ")
    time.sleep(3)
    clear()
    for libs in Mads.mlb3:# Maybe use if statements
      new_libs = libs.replace("1", first)
      new_libs = new_libs.replace("2",second)
      new_libs = new_libs.replace ("3", third)
      new_libs = new_libs.replace ("4", fourth)
      new_libs = new_libs.replace ("5", fifth)
      new_libs = new_libs.replace ("6", sixth)
      new_libs = new_libs.replace ("7", seventh)
      new_libs = new_libs.replace ("8", eighth)
      print(new_libs)

  def mad_lib4():
    first = input("Enter first word(This is should be an noun ): ")
    second = input("Enter second word (This is should be a adjective): ")
    third = input("Enter Third word (This is should be a number): ")
    fourth = input("Enter Fouth word (This is should be an adjective): ")
    fifth = input("Enter Fifth word (This is should be a noun): ")
    sixth = input("Enter sixth word This is should be an proper noun): ")
    seventh = input("Enter seventh word (This is should be an proper noun): ")
    eighth = input("Enter eighth word (This is should be a plural noun): ")
    ninth = input("Enter ninth word (This is should be an -ing verb): ")
    time.sleep(3)
    clear()
    for libs in Mads.mlb4:# Maybe use if statements
      new_libs = libs.replace("1", first)
      new_libs = new_libs.replace("2",second)
      new_libs = new_libs.replace ("3", third)
      new_libs = new_libs.replace ("4", fourth)
      new_libs = new_libs.replace ("5", fifth)
      new_libs = new_libs.replace ("6", sixth)
      new_libs = new_libs.replace ("7", seventh)
      new_libs = new_libs.replace ("8", eighth)
      new_libs = new_libs.replace ("9", ninth)
      print(new_libs)
      
  def mad_gen():
    return None
