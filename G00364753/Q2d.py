# Patrick Moore 2019-03-05
# This is a script to create a function that finds the max value in a list
# using an iterative approach, as directed by Question 2(d) of the 
# Computational Thinking with Algorithms problem sheet

# define a function that takes a list as an argument
def max_iter(data):
  # set the maximum value to be the first item in the list
  maximum = data[0]
  # create a counter variable for the while loop
  counter = 0
  # use a while loop to iterate over the length of the list
  while counter < len(data):
    # check if any item in the list is greater than the current maximum
    if data[counter] > maximum:
      # if so, set maximum to that value
      maximum = data[counter]
    # increment the counter  
    counter = counter + 1
  # once the while loop terminates, return the max value  
  return maximum

# create a variable to store the data list
y = [0, -247, 341, 1001, 741, 22]

# call the finder 
# function
print(max_iter(y))