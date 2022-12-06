with open('input.txt') as f:
    input = f.readlines()


lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
prio = lower_case + upper_case

prio_map = {}

for i,x in enumerate(prio,1):
    prio_map.update({x:i})

sum = 0
temp = []
groups = []
counter = 0
for x in input:
    if counter == 0:
        temp.append(x)
        counter += 1
        continue
    if counter % 3 == 0:
        groups.append(temp)
        temp = []
        temp.append(x)
        counter += 1
    else:
        temp.append(x)
        counter += 1
groups.append(temp)

items = []
for x in groups:
    for y in x[0]:
        if y in x[1] and y in x[2]:
            items.append(y)
            break

for x in items:
    sum += prio_map[x]

print(sum)