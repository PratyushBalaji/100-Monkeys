# 100 Monkeys Problem

This code contains 4 solutions to the 100 monkeys problem, that I arrived at by observing various patterns in the problem. The following text explains each solution, 

## The Problem : 
The problem is simple enough. 

There is a corridor with 100 numbered, closed doors.

100 numbered monkeys are released one by one, with each monkey either closing an open door or opening a closed door. However, they can only interact with doors that are a multiple of their number.

For example : 
- Monkey #30 can only interact with doors 30, 60, and 90. 
- Monkey #100 can only interact with door 100

The goal is to find the doors which remain open after all the monkeys finish running through the corridor.

Although the original problem was about 100 monkeys, these solutions are all made to work with corridors of any length.

## Setup Code

Since each door is either open or closed, it is convenient to consider them booleans. For this implementation, I have considered the corridor to be a boolean array. The doors and monkeys are 1-indexed, but the array is 0-indexed, so all math operations will be performed with an offset of one.

How doors will be stored : 
```python
n = 10000000 # number of doors
doors = [False]*n # corridor of specified length
```

How the open doors will be displayed : 
```python
def openDoors(sol):
    return [x+1 for x,i in enumerate(sol) if i == True]
```

There is an issue with scoping. Since `doors` is global, calling a function with `doors` may lead to it copying the reference and modifying in place, even if you redeclare an array inside it like `ret = doors`. 

I need each function to reinitialise the doors array so it returns a new array each time instead. The simplest way to do this is declaring a local array that is equal to the passed array in all ways except the reference.

I've chosen to do so like this : 
```python
def solutionN(doors):
    returnedArr = doors[:] # copies array in its entirety
    ...
```

## Solution 1 : Brute Force
**Time complexity : O($n^2$)**

**Algorithm :** Outer for loop tracks monkey numbers, inner for loop tracks door numbers. If door number is a multiple of monkey number, open / close that door.

**Code :**
```python
def bruteForce(d):
    ret = d[:]
    for i in range(len(ret)):
        for j in range(len(ret)):
            if (j+1)%(i+1)==0:
                ret[j] = not ret[j]
    return ret
```

Double for loop leads to quadratic complexity. This works but it manually simulates every monkey toggling a door and is highly inefficient. In the rest of the solutions we will see why this is not necessary.

## Solution 2 : Check if a door is a perfect square
**Time complexity : O($n$)**

**Algorithm :** Single for loop going through every door, only leaving those doors open that are perect squares.

**Why this works :**
Every door starts off closed, but is opened and closed several times by the monkeys.

Consider door #4. It is opened by monkey #1, but subsequently closed by monkey #2, and then later opened by monkey #4, which is how it finally remains. 

We observe that each door is toggled exactly the same number of times as it has factors. If it has an even number of factors, it'll just return to its initial state. Every time it is opened, it is closed again.

If we consider the factors of any number, every factor is paired with another to form the original number. Usually, they are paired with disctint factors like so :

$$\text{24 : (1,24), (2,12), (3,8), (4,6)}$$

In the case of square numbers, one of their factors is ($\sqrt n$, $\sqrt n$). But since every monkey only interacts with each door once, this factor pair leads to only one door interaction. Monkey #$\sqrt n$ toggles door #$n$ a single time.

Doors with an odd number of factors are left open, and the only ones with an odd number of factors are perfect squares, hence we only open those doors which are perfect squares.

**Code :**
```python
def checkPerfectSquare(d):
    import math
    ret = d[:]
    for i in range(len(doors)):
        if math.sqrt(i+1) == int(math.sqrt(i+1)):
            ret[i] = True
    return ret
```

## Solution 3 : Square Index Until End
**Time complexity : O($\sqrt n$)**

**Algorithm :** While loop that runs while an initialised counter is less than or equal to the number of doors, and toggles every square, iterating as it goes

**Code :**
```python
def squareNumbers(d):
    ret = d[:]
    i = 1
    while i*i <= len(ret):
        ret[i*i - 1] = True
        i += 1
    return ret
```

Much faster than solution 2 because it doesn't do time-intensive square root operations, and it doesn't traverse the whole array, only setting $\sqrt n$ elements.

## Solution 4 : Square Index (without multiplication)
**Time complexity : O($\sqrt n$)**

**Algorithm :** Keeps track of current index and the next odd number. While index is within bounds, set value at index to `True`, add odd number to index, and store new next odd number.

**Why this works :** Basic algebra tells us that to go from $n^2$ to $(n+1)^2$ we add $2n+1$. $2n+1$ is just the $n$th odd number (0-indexed). By recognising this, instead of incrementing $i$ and overwriting index $i^2$ as we did in the previous solution, we can keep track of an odd number `count`, add the count to `i` for the array overwriting, and add 2 to `count` to make it store the next odd number. This allows us to find every square without doing any multiplication, relying only on addition.

**Code :** 
```python
def squareNumbersWithoutMult(d):
    ret = d[:]
    count = 3 # count starts at 3 since first door toggled is #1
    i=0
    while i<len(ret):
        ret[i]=True
        i+=count
        count+=2
    return ret
```

This solution mostly has the same runtime as the previous one. Benchmarking reveals no difference at all between the algorithms, probably because modern hardware is insanely fast at both multiplication and addition. Multiplication is not that much more inefficient than addition.

However, this could prove useful for situations where addition is preferred over multiplication.