def remove_duplicates(list1):
    not_duplicates = []
    for i in list1:
        repeated = list1.count(i)
        if repeated == 1:
            not_duplicates.append(i)
    return not_duplicates

a = [1,1,2,2,3,4,5,5,6,6,6,7,8]
print(remove_duplicates(a))


