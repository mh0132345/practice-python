def swapLexOrder(str, pairs):
    n = len(str)
    str = list(str)

    corr = [set() for i in range(n)]
    nodes = set()
    for a, b in pairs:
        corr[a-1].add(b-1)
        corr[b-1].add(a-1)
        nodes.add(a-1)
        nodes.add(b-1)

    while nodes:
        active = {nodes.pop()}
        group = set()
        while active:
            group |= active
            nodes -= active
            active = {y for x in active for y in corr[x] if y in nodes}

        chars = iter(sorted((str[i] for i in group), reverse=True))
        for i in sorted(group):
            str[i] = next(chars)

    return "".join(str)