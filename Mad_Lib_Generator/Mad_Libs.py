mlb1 =[ 'This is the 1 madlib to 2 its fucntionality'
]

class MadLibs:

  def __init__(self):
    return None

  def __repr__(self, Madlib_Number):
    return f' Here is your new madlib! {new_libs}'

def mad_lib1():
  first = input("Enter first word: ")
  second = input("Enter second word: ")
  for libs in mlb1:# Maybe use if statements
    new_libs = libs.replace("1", first)
    new_libs = new_libs.replace("2",second)
    print(new_libs)

mad_lib1()