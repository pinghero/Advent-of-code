# open text file and save lines in list 'input'
with open('day-1-input.txt') as f:
    input = f.readlines()

#init counter ,temp (equal to sum of first 3 items) and sum
counter = 0
temp = int(input[0]) + int(input[1]) + int(input[2])
sum = 0

#loop through list and keep current loop index
for index,line in enumerate(input):
    #try - if list index NOT out of range
    try:
        #add current item with next 2 items
        sum = int(line) + int(input[index+1]) + int(input[index+2])
        #compare current sum with previous sum
        if sum > temp:
            counter += 1
        #save current sum to temp for next comparison
        temp = sum
    #except - if list out of range exception (last sum reached) break loop
    except:
        break

#result
print(counter)