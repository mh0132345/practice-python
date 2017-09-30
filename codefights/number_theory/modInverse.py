def modInverse(n, m):
    gcd, x, y = egcd(n, m)
    if gcd != 1:
        return -1
    else:
        return x % m

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)   
