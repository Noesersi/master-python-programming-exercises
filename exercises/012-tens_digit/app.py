#Complete the function to return the tens digit of a given interger
def tens_digit(num):
  string_num= str(num)
  last2= string_num[-2:]
  result= int(last2[0])
  return result




#Invoke the function with any interger.
print(tens_digit(156))