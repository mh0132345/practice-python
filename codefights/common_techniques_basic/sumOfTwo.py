def sumOfTwo(a, b, v):
    a = set(a)
    b = set(b)
    for i in a:
        if (v-i) in b:
            return True
    return False

