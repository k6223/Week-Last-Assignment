#Kollin Schalhamer
#Dr Neumann
#CIS-125
#4 December 2015
#subsetCompare.py

import math
import time
def subsetI(n,k):
    return math.factorial(n) / (math.factorial(k)* math.factorial(n-k))

def subsetR(n,k):
    if n==k:
       return 1
    if k==0:
        return 1
    else:
        return subsetR(n-1,k-1)+subsetR(n-1,k)
        


def main():
    n = 20
    k = 5
    loops=1000

    timeB = time.time()
    for x in range(loops):
        I = subsetI(n,k)
    timeA = time.time()
    print("I = ",I)
    print("elapsed time: ", timeA-timeB)

    timeB = time.time()
    for x in range(loops):
        R = subsetR(n,k)    
    timeA = time.time()
    print("R = ",R)
    print("elapsed time: ", timeA-timeB)
 
if __name__=="__main__":
    main()