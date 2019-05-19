import math

def kickstartAlarm(): 
    
    '''
    Problem Complete Description at:
    https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/0000000000058a56

    - Read from stdin.
    - Create a table according to problem description
    - Calculate summation of the each exponential-power of every case
    - Send results to stdout.

       Input 
       =====
        2
        2 3 1 2 1 2 1 1 9
        10 10 10001 10002 10003 10004 10005 10006 89273

        Output 
        ======
        Case #1: 52
        Case #2: 739786670 
    
    '''
    
    values = [] 
    t = int(input())
    result = 0
    module = 1000000007

    
    for case in range(1, t + 1):
        line = input().split(" ")
        N = int(line[0])
        K = int(line[1])
        x1 = int(line[2])
        y1 = int(line[3])
        C = int(line[4])
        D = int(line [5])
        E1 = int(line [6])
        E2 = int(line [7])
        F = int(line [8]) 
        
         
        first = (x1 + y1) % F
        
        values.append(first)
        
        for length in range(1, N):
            x = (C*x1 + D*y1 + E1)%F 
            y = (D*x1 + C*y1 + E2)%F
            values.append((x + y)% F) 
            x1 = x
            y1 = y
            
        for i in range(1,K+1): 
            result = (solve(values, i) + result) % module

        print("Case #{0}: {1}".format(case,result))
            
        result = 0
        values.clear()
            

def solve(values, i):
    ''' (list of int) --> int

    Result is just the summation of the i exponential-power
    of all the contiguous subarrays of the Parameter Array.  

    >>> result([1,4,2],2)
    >>> 71

    '''
    result = 0 
    occurrence = 0
    index = 0
    module = 1000000007

    
    for k in range (len(values)):
        index = index + 1
        for j in range (k, len(values)):
            semiResult = (values[j] * index**i) % module
            occurrence = len(values) - j
            result =  ((semiResult * occurrence) + result) % module
            

    return result        
        
            
         
    
        
        
     
    

    
        
      

    
