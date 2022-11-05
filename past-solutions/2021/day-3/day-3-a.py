# open text file and save lines in list 'input'
with open('day-3-input.txt') as f:
    input = f.readlines()

#init help variables
zeroes = 0
ones = 0
gamma_rate_str = ""
epsilon_rate_str = ""

#loop 12 times (length of input strings)
for i in range(0,12):
    #loop for every line in input
    for line in input:
        #bit = current string's i position (0 to 12)
        bit = line[i]
        #count zeroes and ones for line at position i    
        if int(bit) == 0:
            zeroes += 1
        else:
            ones += 1
    #compare 0s and 1s and add appropriate bit to gamma and epsilon strings
    if zeroes > ones:
        gamma_rate_str += '0'
        epsilon_rate_str += '1'
    else:
        gamma_rate_str += '1'
        epsilon_rate_str += '0'
    #clear counters for next loop
    ones = 0
    zeroes = 0

#convert gamma and epsilon strings to int
#int(string,2) converts a string of ones and zeroes to the integer they represent in binary
gamma_rate_int = int(gamma_rate_str,2)
epsilon_rate_int = int(epsilon_rate_str,2)

result = gamma_rate_int * epsilon_rate_int

print(result)


