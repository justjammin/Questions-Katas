input = "racecar"

input = str(input)

def missyElliot(input):
  return input[::-1]

reversed = missyElliot(input)

if input != reversed:
  print(False)
else: 
  print(True)