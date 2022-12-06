
with open('input.txt') as f:
    input = f.readlines()

points = {'A':1,'B':2,'C':3}
mapping = {'A':{'X':'C','Y':'A','Z':'B'},'B':{'X':'A','Y':'B','Z':'C'},'C':{'X':'B','Y':'C','Z':'A'}}
score = 0

for x in input:
    match x[2]:
        case 'X':
            score += points[mapping[x[0]]['X']]
        case 'Y':
            score += 3 + points[mapping[x[0]]['Y']]
        case 'Z':
            score += 6 + points[mapping[x[0]]['Z']]   

print(score)