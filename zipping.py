#!D:\Aplikasi\Program\Python\python.exe

list_1 = [1, 2, 3]
list_2 = ["one", "two", "three", "four"]
list_3 = ["siji", "loro", "telu"]
print(list(zip(list_1, list_2, list_3)))
# Cuma bisa satu key satu value
print(dict(zip(list_1, list_2)))
