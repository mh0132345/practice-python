def areFollowingPatterns(strings, patterns):
    group = {}
    for string, pattern in zip(strings, patterns):
        if string in group and group[string] != pattern:
            return False
        group[string] = pattern
    return len(group) == len(set(group.values()))
