def minSubstringWithAllChars(s, t):
    for x in range(len(s)+1):
        for p in range(len(s)-x+1):
            c = filter(lambda x: x in t,s[p:p+x])
            if len(set(c))==len(t):
                return s[p:p+x]
    return ""

