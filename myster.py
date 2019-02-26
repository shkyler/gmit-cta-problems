# Patrick Moore 2019-02-23
# This is a script to test the algorithm in Question 1 of the 
# Computational Thinking with Algorithms problem sheet

def mystery(n):
  # the function program first prints the number passed to it
  print(n)
  # if the number is less than 4 if the function calls itself 
  # for n + 1 (this will repeat until n = 4)
  if n < 4:
    mystery(n + 1)
  # once the condtion in the if statement is met the function 
  # moves onto the the final line and prints the final value of n
  # the function will trace back and close each of the "open" instances of the function  
  print(n)

# caLL the function by passing the value '1' to it
mystery(1)  

'''
def fact(n):
  if n <=1 :
    return 1
  else: 
    return n * fact(n-1)
'''