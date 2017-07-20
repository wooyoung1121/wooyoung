def avg(things):
    return sum(things)/len(things)

thousand_numbers = []

for i in range(0,1000000):
    from random import randint

    thousand_numbers.append(randint(0, 100))

print (thousand_numbers)
print (sum(thousand_numbers)/len(thousand_numbers))