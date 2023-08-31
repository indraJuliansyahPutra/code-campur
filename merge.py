#!D:\Aplikasi\Program\Python\python.exe

def merge(list_1, list2):
  list_1.sort()
  list_2.sort()
  list_baru = list_1 + list_2
  return list_baru

list_1 = [5, 3, 2, 6, 1]
list_2 = [9, 7, 10, 4, 8]
print(merge(list_1, list_2))
