#Part 1
count = 0
for i in range(len(lines)):
    number1 = ""
    number2 = ""
    j = 0
    while number1 == "":
        if lines[i][j].isnumeric():
            number1 = lines[i][j]
        j+=1
    l = len(lines[i])-1
    while number2 == "":
        if lines[i][l].isnumeric():
            number2 = lines[i][l]
        l-=1
    number = number1 + number2
    count += int(number)

print(count)
