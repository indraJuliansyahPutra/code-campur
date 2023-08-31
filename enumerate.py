list = [1, 2, 98, 5, -1, 2, 0, 5, 10]
counter = 0
for i, x in enumerate(list):
  if x == 5:
    counter += 1
    if counter == 2:
      break

print(i)
