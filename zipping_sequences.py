days = "Monday Tuesday Wednesday Thursday".split()
weathers = "Sunny Rainy Cloudy Yuny".split()
temperatures = [12, 10, 34, 29]

for day, weather, temperature in zip(days, weathers, temperatures):
  print("On {} it was {} and the temperatures was {} defress celcius".format(day, weather, temperature))
