#Complete the function to return:
#1) How many apples each single student will get.
#2) How many apples wil remain in the basket.
#Hint: You can resolve this exercise either importing the math module or without it 
def apple_sharing(n,k):
  apple_for_each= k // n
  residual_apples= k % n
  
  return apple_for_each, residual_apples
 
    

#Print the two answer per the example output.
print(apple_sharing(6,50))