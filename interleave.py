def interleave(list_1, list_2):
  gabungan = []
  for item_1, item_2 in zip (list_1, list_2):
    gabungan.append(item_1)
    gabungan.append(item_2)
  return gabungan

list_1 = [1, 2, 3]
list_2 = ["one", "two", "four"]
print(interleave(list_1, list_2))
