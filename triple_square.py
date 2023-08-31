#!D:\Aplikasi\Program\Python\python.exe

def triple(number):
  return number * 3

def square(number):
  return number ** 2

def main():
  for i in range(1, 11):
    if (square(i) > triple(i)):
      break
    else:
      print("triple ({}) == {} square({}) == {}".format(i, triple(i), i, square(i)))

main()
