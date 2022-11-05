# open text file and save lines in list 'input'
with open('day-1-input.txt') as f:
    input = f.readlines()

#init counter and temp (equal to first list item)
counter = 0
temp = input[0]

#loop through list and compare current list item to previous saved in variable 'temp'
for line in input:
    #if current element > previous element -> counter ++
    if int(line) > int(temp):
        print(int(line))
        counter += 1
    temp = line

#result
print(counter)
