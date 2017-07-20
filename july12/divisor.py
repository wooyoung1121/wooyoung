def get_divisors (input):
    divisors = []
    for i in range (1,input + 1):
        if input%i == 0:
            divisors.append(i)

    return divisors

print (get_divisors (57))