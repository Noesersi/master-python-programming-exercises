#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
  stringD = str(digit)
  return int(stringD[0]), int(stringD[1])
   


#Invoke the function with any interger as its argument.
print(two_digits(79))
