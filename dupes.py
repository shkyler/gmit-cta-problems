def dupes(elements):
    # create a variable to count the comparisons made
    count = 0
    # use nested for loops to compate the items in the list
    for i in range(0, len(elements)):
        for j in range(0, len(elements)):
            # avoid self comparison
            if i == j:
                continue  
            # if the elements match, increment the counter and return the final value    
            if elements[i] == elements[j]:
                count = count + 1
                return count
            # otherwise increment the counter
            else:
                count = count + 1  
    # if no match is found return the final value of the counter            
    return count

a = [10,0,5,3,-19,5] 
b = [0,1,0,-127,346,125]
print(dupes(a))
print(dupes(b))

#import time
#start = time.time()
#a = [10,0,5,3,-19,5] 
#b = [0,1,0,-127,346,125]
#print(dupes(a))
#end = time.time()

#print("Runtime is: " + str(end - start))

