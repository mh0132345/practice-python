def firstNotRepeatingCharacter(s):    
    letters = []
    flag = [False]*26
    for ch in s:
        if flag[ord(ch)-ord('a')]:
            if ch in letters:
                letters.remove(ch)            
        else:
            letters.append(ch)
            flag[ord(ch)-ord('a')] = True
    if len(letters) == 0:
        return '_'
    else:
        return letters[0]
