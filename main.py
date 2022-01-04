input = "1221"

input = str(input)

def missyElliot(input):
  return input[::-1]

reversed = missyElliot(input)

print(bool(input == reversed))

