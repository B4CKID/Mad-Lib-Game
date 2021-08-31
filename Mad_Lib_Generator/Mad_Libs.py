from Mad_Lib_Storage.Madlib_Text import mlb1


class MadLibs:

  def __init__(self):
    return None

  def __repr__(self):
    return f' Here is your new madlib! {new_libs}'

def mad_lib1():
  first = input("Enter first word: ")
  second = input("Enter second word: ")
  third = input("Enter Third word: ")
  fourth = input("Enter Fouth word: ")
  fifth = input("Enter Fifth word: ")
  for libs in mlb1:# Maybe use if statements
    new_libs = libs.replace("1", first)
    new_libs = new_libs.replace("2",second)
    new_libs = new_libs.replace ("3", third)
    new_libs = new_libs.replace ("4", fourth)
    new_libs = new_libs.replace ("5", fifth)
    print(new_libs)

mad_lib1()