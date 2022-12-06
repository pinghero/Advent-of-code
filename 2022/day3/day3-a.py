with open('input.txt') as f:
    input = f.readlines()

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
prio = lower_case + upper_case

prio_map = {}

for i,x in enumerate(prio,1):
    prio_map.update({x:i})

sum = 0

for x in input:
    for y in x[:len(x)//2]:
        if y in x[len(x)//2:]:
            print(y)
            sum += prio_map[y]
            break

print(sum)