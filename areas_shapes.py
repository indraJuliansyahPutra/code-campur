#!D:\Aplikasi\Program\Python\python.exe

def rectangle():
  width = float(input("Give width of the rectangle: "))
  height = float(input("Give height of the rectangle: "))
  area = width * height
  return "The area is {}".format(area)

def triangle():
  base = float(input("Give base of the triangle: "))
  height = float(input("Give height of the triangle: "))
  area = 0.5 * base * height
  return "The area is {}".format(area)

def circle():
  pi = 3.14
  radius = float(input("Give radius of the circle: "))
  area = pi * (radius ** 2)
  return "The area is {}".format(area)

def main():
  while True:
    shape = input("Choose a shape (triangle, rectangle, circle): ")
    if shape.lower() == "rectangle":
      result = rectangle()
    elif shape.lower() == "triangle":
      result = triangle()
    elif shape.lower() == "circle":
      result = circle()
    elif shape.lower() == "":
      result = "Unknown Shape!"
    else:
      break
    print(result)

if __name__ == "__main__":
  main()
