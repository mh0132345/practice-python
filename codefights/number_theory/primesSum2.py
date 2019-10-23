def primesSum2(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    p=2
    while(p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p+=1
    sum = 0
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            sum += p
    return sum%(10**9+7)


