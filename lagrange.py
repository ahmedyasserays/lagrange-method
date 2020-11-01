def multiply_two(first, second):
    result = ""
    # first term
    if first[0] == "x" and second[0] == "x":
        result += "x^2"
    else:
        print("please review the first term of the multiply two function")

    # second term
    if "--" in first:   # fixes the double minus sign problem
        first_list = list(first)
        first_list[2] = "+"
        first = "".join(first_list)
    if "--" in second:
        second_list = list(second)
        second_list[2] = "+"
        second = "".join(second_list)
    term = int(first[-2:]) + int(second[-2:])   # find the factor of x
    if term > 0:    # set the plus or minus sign
        result += "+" + str(term) + "x"
    elif term < 0:
        result += str(term) + "x"

    # last term
    if "--" in first:
        first_list = list(first)
        first_list[2] = "+"
        first = "".join(first_list)
    if "--" in second:
        second_list = list(second)
        second_list[2] = "+"
        first = "".join(second_list)
    term = int(first[-2:])*int(second[-2:])
    if term > 0:
        result += "+" + str(term)
    elif term < 0:
        result += str(term)

    return result

def multiply_three(two, three):
    result = ""
    if "--" in two:  # fixes the double minus sign problem
        two_list = list(two)
        two_list[2] = "+"
        two = "".join(two_list)

    # first term
    if two[0] == "x" and three[0:3] == "x^2":
        result += "x^3"
    else:
        print("please review the first term in the multiply three function")

    # second term
    try:
        if two[0] == "x" and three[5] == "x":
            term = int(three[3:5])+int(two[-2:])
            if term >= 0:
                result += "+"
            result += str(term) + "x^2"
        else:
            print("please review the second term in the multiply three function")
    except IndexError:
        if len(three) > 3:
            result += two[-2:] + "x^2"
        else:
            print("please review the second term again")
    # third term
    if three[-1] != "x" and len(three) == 8:
        term = (int(two[-2:])*int(three[3:5])) + int(three[-2:])
        if term >= 0:
            result += "+"
        result += str(term) + "x"
    elif three[-1] != "x" and 3 < len(three) < 8:
        if int(three[-2:]) > 0:
            result += "+"
        result += three[-2:] + "x"
    elif three[-1] == "x" and 3 < len(three) < 8:
        if int(three[3:5]) >= 0:
            result += "+"
        result += three[3:5] + "x"
    else:

        result += str(int(two[-2:])*int(three[3:5])) + "x"


    # forth term
    if len(three) > 3 and three[-1] != "x":
        term = int(two[-2:]) * int(three[-2:])
        if term >= 0:
            result += "+"
        result += str(term)

    return result


p = []
x_values = []
y_values = []

# getting inputs
n = int(input("how many X and Y values do you know?\n"))

for i in range(n):
    x_values.append(input("please enter the number " + str(i + 1) + " x value: "))
    y_values.append(input("please enter the number " + str(i + 1) + " y value: "))

# creating the p
for j in range(n):
    if j == 0:
        p.append([])
        continue
    p.append([])

    # calculating every p
    for i in range(n):

        if i == j:
            continue

        p[j].append("x-" + x_values[i])
        p[j].append(int(x_values[j]) - int(x_values[i]))

    # calculating the up and down values
    up = ""
    down = 1
    for i in range(len(p[j])):
        if i % 2 == 0:
            if i == 0:
                up = up + p[j][i]
            else:
                up = up + " * " + p[j][i]

        else:
            down *= p[j][i]

    print(up)
    print(down)
    for i in range(len(p[j])):
        if i % 2 == 0:
            if i == 0:
                continue
            print(multiply_two(p[j][i], p[j][i - 2]))
print(multiply_three("x--1", "x^2-3x"))
