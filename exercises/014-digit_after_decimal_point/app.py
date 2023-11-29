#Complete the function to return the first digit to the right of the decimal point.
import math
def first_digit(num):
  decimals = num % 1
  print(decimals)
  stringed_decimals= str(decimals)
  result = int(stringed_decimals[2])

  return result

#Invoke the function with a positive real number. ex. 34.33
print(first_digit(1.89))