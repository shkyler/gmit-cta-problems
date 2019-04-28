# Patrick Moore 2019-03-03
# This is a script to test the algorithm in Question 2 of the 
# Computational Thinking with Algorithms problem sheet

# define a function that takes a list as an argument
def finder(data): 
  # call the finder_rec() function by passing the orignal list,
  # and the index of the last item in the list as arguments
  return finder_rec(data, len(data)-1)

# define a function that takes a list and an integer as arguments
def finder_rec(data,x):
  # if x is zero - return the first item in the list (base case for recursion)
  if x == 0:
    return data[x]
  # otherwise set v1 to be the value of the item in that position in the list  
  v1 = data[x]
  # v2 is set by calling the finder_rec() function for the previous item in the list
  v2 = finder_rec(data, x-1)
  # once we have reached the base case it will the compare each item in the list,
  # returning the greatest number each time
  # ultimately it will return the greatest number in the list
  if v1 > v2:
    return v1
  else:
    return v2

# create a variable to store the data list
y = [0, -247, 341, 1001, 741, 22]

# call the finder function
finder(y)
