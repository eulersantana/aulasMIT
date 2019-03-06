import random 
import Aula1 as a1

def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(a1.Food(str(i), 
                             random.randint(1, maxVal),
                             random.randint(1, maxCost)))
    return items

for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60):
    items = buildLargeMenu(numItems, 90, 250)
    a1.testGreedyRecursive(items, 750 )
    
###############################################################################


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fastFib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n -1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result 

print(fastFib(120))