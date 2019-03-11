# Patrick Moore 2019-03-05
# This is a script to test Q3 of the f the 
# Computational Thinking with Algorithms problem sheet

def duplicates(elements):
  comparisons = 0
  i = 0
  j = 0
  while i < len(elements):
    comparisons = comparisons + 1
    print(comparisons)
    while j < len(elements):
      comparisons = comparisons + 1
      print(comparisons)
      if i == j:
        continue  
      if elements[i] == elements[j]:
        break
      j = j + 1
  i = i + 1    
  return comparisons

y =[1,2,3,4]
print(duplicates(y))