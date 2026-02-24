def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)    #condition or Stopping condition
    
print(fact(5))