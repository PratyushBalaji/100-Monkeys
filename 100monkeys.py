'''
Problem : 
100 monkeys are released one by one, with each monkey either closing an open door, or opening a closed door. 
However, they can only interact with doors that are a multiple of their number.
    (monkey #30 can only interact with doors 30, 60 and 90)
Find the open doors after all the monkeys had finished their interactions.
'''
n = 5000000
doors = [False]*n

# Approach 1 : Brute Force (Quadratic complexity)
def bruteForce(d):
    ret = d[:]
    for i in range(len(ret)):
        for j in range(len(ret)):
            if (j+1)%(i+1)==0:
                ret[j] = not ret[j]
    return ret

# Approach 2 : Square Root to Check Squares (Linear complexity)
def checkPerfectSquare(d):
    import math
    ret = d[:]
    for i in range(len(doors)):
        if math.sqrt(i+1) == int(math.sqrt(i+1)):
            ret[i] = True
    return ret

# Approach 3 : Square Index Until End (Square Root complexity)
def squareNumbers(d):
    ret = d[:]
    i = 1
    while i*i <= len(ret):
        ret[i*i - 1] = True
        i += 1
    return ret
    
# Approach 4 : Using increasing odd spacing between squares to find index (Square Root complexity)
def squareNumbersWithoutMult(d):
    ret = d[:]
    count = 3
    i=0
    while i<len(ret):
        ret[i]=True
        i+=count
        count+=2
    return ret

def openDoors(sol):
    return [x+1 for x,i in enumerate(sol) if i == True]


# Simple benchmark
# Uses time module so for small input sizes, time may not register.
# Increasing door size above 10e6 makes brute force extremely slow 
# Comment out bruteForce tests for larger corridors, and checkPerfectSquare for very large corridors
import time
curr = time.time()
bruteForce(doors)
print(f"Brute Force : {time.time()-curr}")

curr = time.time()
checkPerfectSquare(doors)
print(f"Check Perfect Square (sqrt) : {time.time()-curr}")

curr = time.time()
squareNumbers(doors)
print(f"Square Indices (mult) : {time.time()-curr}")

curr = time.time()
squareNumbersWithoutMult(doors)
print(f"Square Indices (add) : {time.time()-curr}")

# Check factor by which algorithm is faster
# import time
# arr = []
# for i in range(500):
#     curr = time.time()
#     squareNumbers(doors)
#     t1 = time.time()-curr

#     curr = time.time()
#     squareNumbersWithoutMult(doors)
#     t2 = time.time()-curr

#     arr.append(t2/t1)
    
# # print(arr)
# print(sum(arr)/len(arr))