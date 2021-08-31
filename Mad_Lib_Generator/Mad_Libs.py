from Mad_Lib_Storage.Madlib_Text import mlb1


class MadLibs:

  def __init__(self):
    return None

  def __repr__(self):
    return new_libs

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
    for libs in mlb1:# Maybe use if statements
      new_libs = libs.replace("1", first)
      new_libs = new_libs.replace("2",second)
      new_libs = new_libs.replace ("3", third)
      new_libs = new_libs.replace ("4", fourth)
      new_libs = new_libs.replace ("5", fifth)
      new_libs = new_libs.replace ("6", sixth)
      new_libs = new_libs.replace ("7", seventh)
      new_libs = new_libs.replace ("8", eighth)
      new_libs = new_libs.replace ("9", ninth)
      new_libs = new_libs.replace ("10", tenth)
      print(new_libs)

