import math

def sieve_prime(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p**2 <= n):      
        if (prime[p] == True):              
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return(prime)

while(True):
    num = float(input())
    if (num == 0):
        break
    prime = sieve_prime(math.floor(num*(10**3)))
    for i in range (1,4):
        check = math.floor(num*(10**i))
        is_prime = (prime[check])
    if (is_prime):
        print("TRUE")
    else:
        print("FALSE")