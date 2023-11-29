#Complete the function to return the respective number of the century
#HINT: You may need to import the math module.
import math

def century(year):
  if year % 100 == 0:
    return int(str(year)[:2])
  if year % 100 != 0:
    return int(str(year)[:2])+1




#Invoke the function with any given year. 
print(century(2000))
print(century(1900))
print(century(1990))

