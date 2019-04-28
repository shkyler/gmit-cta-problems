# Patrick Moore 2019-03-03
# This is a script to test the algorithm in Question 2 of the 
# Computational Thinking with Algorithms problem sheet

def finder(data):
  return finder_rec(data, len(data)-1)

def finder_rec(data,x):
  print("____________")
  print("x: " + str(x))
  if x == 0:
    print("____________")
    return data[x]
  v1 = data[x]
  print("v1: " + str(v1))
  v2 = finder_rec(data, x-1)
  print("x: " + str(x))
  print("v1: " + str(v1))
  print("v2: " + str(v2))
  print("____________")
  if v1 > v2:
    return v1
    print(v1)
  else:
    return v2
    print(v2)

y = [0, -247, 341, 1001, 741, 22]

finder(y)
