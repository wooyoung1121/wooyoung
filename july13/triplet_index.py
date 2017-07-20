def get_index(list):
    for number in list:
        maximum = max(list)
        minimum = min(list)
        middle_number = sum(list) - (maximum+minimum)
        index = list.index(middle_number)
    return (index)
a = (4,7,5)
print(get_index(a))
