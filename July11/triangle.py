def check_triangle(sides):

    longest = max(sides)
    the_rest = sum(sides) - longest
    print(longest, the_rest)
    return the_rest > longest

side1 = input("enter length of side 1: ")
side2 = input("enter length of side 2: ")
side3 = input("enter length of side 3: ")
string_sides = [side1, side2, side3]
float_sides = list(map(float, string_sides))

print(check_triangle(float_sides))
