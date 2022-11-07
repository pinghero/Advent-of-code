input = []
temp = []
with open('day-4-input.txt') as f:
    draw = f.readline().split(",")
    draw[-1] = draw[-1].strip()
    for line in f:
        temp.append(line.rstrip().split())
        input.append(temp)
print(input)
def check_horizontal(input,list):
    sum = -1
    for row in list:
        if row:
            # print(row,"\n")
            if row[0] in input and row[1] in input and row[2] in input and row[3] in input and row[4] in input:
                for element in row:
                    if element not in input:
                        sum += int(element)
                        print("found", row)
                        return sum
    return 0

def check_vertical(input,list):
    for row in list:
        if row:
            if row[0] in input and list[5] in input and list[10] in input and list[15] in input and list[20] in input:
                print("found")
                return 1
            else:
                continue
    return 0


with open('day-4-input.txt') as f:
    for line in f:
            input.append(line.rstrip().split())

draw1 = []
for element in draw:
    draw1.append(element)
    x = check_horizontal(draw1,input)
    if x != 0:
        print(x+int(draw1[-1]))
    if check_vertical(draw1,input) == 1:
        break



