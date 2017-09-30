def isCryptSolution(crypt, solution):
    key = {}
    for i in range(0, len(solution)):
        key[solution[i][0]] = int(solution[i][1])
    print(key)
    
    word1 = 0
    word2 = 0
    word3 = 0
    
    for i in range(3):
        if key[crypt[i][0]] == 0 and len(crypt[i]) > 1:
            return False
    
    for i in crypt[0]:
        word1 *= 10
        word1 += key[i]
    for i in crypt[1]:
        word2 *= 10
        word2 += key[i]
    for i in crypt[2]:
        word3 *= 10
        word3 += key[i]
        
    return word3 == word1 + word2

