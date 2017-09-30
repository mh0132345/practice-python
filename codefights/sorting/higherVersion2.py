def higherVersion2(ver1, ver2):
    list1 = ver1.split('.')
    list2 = ver2.split('.')
    for i in range(len(list1)):
        num1 = int(list1[i])
        num2 = int(list2[i])
        if num1 == num2:
            continue
        if num1 < num2:
            return -1
        else: 
            return 1
    return 0

