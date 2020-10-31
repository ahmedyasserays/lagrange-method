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
        first_list[2].replace("-", "+")
        first_list[1].
    if "--" in second:
        second_list = list(second)
        second_list[2] = "+"
        second = "".join(second_list)
    term = int(first[-2:]) + int(second[-2:])   # find the factor of x
    if term > 0:    # set the plus or minus sign
        result += " + " + str(term) + "x"
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

n = int(input("how many X and Y values do you know?\n"))
p = []
x_values = []
y_values = []

# getting inputs
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
