def minimumNumberOfBoxes(a, b, f):
    a,b = max(a,b), min(a,b)
    if a == 0:
        if f!=0:
            return -1 
        return 0
    if b == 0:
        if f%a != 0:
            return -1
        return f//a
    highest_a_boxes = f//a
    for i in range(highest_a_boxes, -1, -1):
        if (f-i*a) % b == 0:
            return i + (f-i*a)//b
    return -1
