#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  stringN= str(num)
  return int(stringN[1]+stringN[0])
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))
print(swap_digits(39))

