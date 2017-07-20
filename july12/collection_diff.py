def get_difference(list1,list2):
    difference = []
    for item in list1:
        if item not in list2:
            difference.append(item)
    for item in list2:
        if item not in list1:
            difference. append(item)
    return difference

a = [1,2,3,4]
b = [4,5,6,7]
print (get_difference(a,b))
