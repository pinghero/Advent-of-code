# open text file and save lines in list 'input'
with open('day-3-input.txt') as f:
    input = f.readlines()

#function to eliminate invalid items from the list
def elimination(list,bit,position):
    result_list = []
    #loop through list parameter
    for line in list:
        #if bit of item at designated position is equal to the bit parameter (0 or 1)
        if int(line[position]) == bit:
            #add list item to result_list
            result_list.append(line)
    #return new list with only valid items
    return result_list

#function to iterate through list and type of iteration (for oxygen or co2)
def iteration(list,type):

    #init counter variables
    ones = 0
    zeroes = 0

    #loop 12 times (length of input strings)
    for i in range(0,12):
        if len(list) == 1:
            break
        #loop for every line in list
        for line in list:
            #bit = current string's i position (0 to 12)
            bit = line[i]
            #count zeroes and ones for line at position i    
            if int(bit) == 0:
                zeroes += 1
            else:
                ones += 1
        #compare 0s and 1s and call elimination function based on the type (oxygen or co2)
        #returned list will have the invalid items removed
        if ones >= zeroes:
            if type == 'oxygen':
                list = elimination(list,1,i)
            elif type == 'co2':
                list = elimination(list,0,i)
        else:
            if type == 'oxygen':
                list = elimination(list,0,i)
            if type == 'co2':
                list = elimination(list,1,i)
        #clear counters for next loop
        ones = 0
        zeroes = 0
    return list

#call function for oxygen and co2
oxygen_list = iteration(input,"oxygen")
co2_list = iteration(input,"co2")

#remove last char of list (python adds a new line char at the end of list)
oxygen_list = oxygen_list[-1].strip()
co2_list = co2_list[-1].strip()
#convert list to string
oxygen_str = "".join(oxygen_list)
co2_str = "".join(co2_list)

#convert string to int according to their binary represantation
oxygen = int(oxygen_str,2)
co2 = int(co2_str,2)

#result
result = oxygen*co2

print(result)