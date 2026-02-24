def check_prime(fact):
    if fact <= 1:
        return False
    
    for i in range(2, fact):
        if fact % i == 0:
            return False
        
    return True 

if check_prime(5):
    print("Prime number")
else:
    print("Not a prime number")

