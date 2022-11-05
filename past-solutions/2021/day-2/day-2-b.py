# open text file and save lines in list 'input'
with open('day-2-input.txt') as f:
    input = f.readlines()

#horizontal position
x_axis = 0
#vertical position
y_axis = 0
#aim
aim = 0
#loop through input list
for line in input:
    #split instruction (separated by space) into temp list
    temp = line.split()
    #switch case for first temp item (instruction)
    match temp[0]:
        #for 'forward' increase horizontal position by second list item (value) and depth by aim * second list item (value)
        case "forward":
            x_axis += int(temp[1])
            y_axis +=  aim * int(temp[1])
        #for 'down' increases aim
        case "down":
            aim += int(temp[1])
        #for 'down' decreases aim
        case "up":
            aim -= int(temp[1])

result = x_axis * y_axis
print(result)