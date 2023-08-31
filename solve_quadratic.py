#!D:\Aplikasi\Program\Python\python.exe
import math

def solve_quadratic(a, b, c):
  result_one = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
  result_two = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
  return "({}, {})".format(result_one, result_two)

number = input("Masukkan Angka: ")
a, b, c = map(float, number.split())
print(solve_quadratic(a, b, c))
