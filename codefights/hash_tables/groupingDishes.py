def groupingDishes(dishes):
    group = {}
    for dish, *ingredients in dishes:
        for i in ingredients:
            group.setdefault(i, []).append(dish)
    
    # check ingredients with more than 2 dishes and add to list
    result = []
    for i in sorted(group):
        if len(group[i]) >= 2:
            result.append([i] + sorted(group[i]))
    return result

