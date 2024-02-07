from collections import defaultdict

def MultipleAlignment(a: str, b: str, c: str):
    weight = defaultdict()
    predecessor = defaultdict()

    weight[0, 0, 0] = 0

    for d in range(1, len(a)+1):
        weight[(d, 0, 0)] = 0
        predecessor[(d, 0, 0)] = (d-1, 0, 0)
    for e in range(1, len(b)+1):
        weight[(0, e, 0)] = 0
        predecessor[(0, e, 0)] = (0, e-1, 0)
    for f in range(1, len(c)+1):
        weight[(0, 0, f)] = 0
        predecessor[(0, 0, f)] = (0, 0, f-1)

    for d in range(1, len(a)+1):
        for e in range(1, len(b)+1):
            weight[(d, e, 0)] = 0
            predecessor[(d, e, 0)] = (d-1, e-1, 0)
    for e in range(1, len(b)+1):
        for f in range(1, len(c)+1):
            weight[(0, e, f)] = 0
            predecessor[(0, e, f)] = (0, e-1, f-1)
    for d in range(1, len(a)+1):
        for f in range(1, len(c)+1):
            weight[(d, 0, f)] = 0
            predecessor[(d, 0, f)] = (d-1, 0, f-1)


    for i in range(1, len(a)+1):
            for j in range(1, len(b)+1):
                for k in range(1, len(c)+1):
                    one = weight[(i-1, j, k)] 
                    two = weight[(i, j-1, k)]
                    three = weight[(i, j, k-1)]
                    four = weight[(i-1, j-1, k)]
                    five = weight[(i, j-1, k-1)]
                    six = weight[(i-1, j, k-1)]
                    
                    if a[i-1] == b[j-1] == c[k-1]:
                        seven = weight[(i-1, j-1, k-1)] + 1
                    else:
                        seven = weight[(i-1, j-1, k-1)]
                    
                    weight[(i, j, k)] = max(one, two, three, four, five, six, seven)

                    if weight[(i, j, k)] == seven:
                        predecessor[(i, j, k)] = (i-1, j-1, k-1)
                    elif weight[(i, j, k)] == six:
                        predecessor[(i, j, k)] = (i-1, j, k-1)
                    elif weight[(i, j, k)] == five:
                        predecessor[(i, j, k)] = (i, j-1, k-1)
                    elif weight[(i, j, k)] == four:
                        predecessor[(i, j, k)] = (i-1, j-1, k)
                    elif weight[(i, j, k)] == three:
                        predecessor[(i, j, k)] = (i, j, k-1)
                    elif weight[(i, j, k)] == two:
                        predecessor[(i, j, k)] = (i, j-1, k)
                    elif weight[(i, j, k)] == one:
                        predecessor[(i, j, k)] = (i-1, j, k)

    length = weight[(len(a), len(b), len(c))]

    current = (len(a), len(b), len(c))

    string1 = ''
    string2 = ''
    string3 = ''

    while not current == (0, 0, 0):
        #print(current)
        prev = predecessor[current]

        if prev == (current[0]-1, current[1], current[2]):
            string1 = a[current[0]-1] + string1
            string2 = '-' + string2 
            string3 = '-' + string3 
        elif prev == (current[0], current[1]-1, current[2]):
            string1 = '-' + string1
            string2 = b[current[1]-1] + string2 
            string3 = '-' + string3 
        elif prev == (current[0], current[1], current[2]-1):
            string1 = '-' + string1
            string2 = '-' + string2 
            string3 = c[current[2]-1] + string3 
        elif prev == (current[0]-1, current[1]-1, current[2]):
            string1 = a[current[0]-1] + string1
            string2 = b[current[1]-1] + string2 
            string3 = '-' + string3 
        elif prev == (current[0], current[1]-1, current[2]-1):
            string1 = '-' + string1
            string2 = b[current[1]-1] + string2 
            string3 = c[current[2]-1] + string3 
        elif prev == (current[0]-1, current[1], current[2]-1):
            string1 = a[current[0]-1] + string1
            string2 = '-' + string2 
            string3 = c[current[2]-1] + string3 
        elif prev == (current[0]-1, current[1]-1, current[2]-1):
            string1 = a[current[0]-1] + string1
            string2 = b[current[1]-1] + string2 
            string3 = c[current[2]-1] + string3 

        current = prev
    
    result = (length, string1, string2, string3)

    return result

file = open('Chapter5(2)\dataset_865453_5.txt')

a = file.readline().strip()
b = file.readline().strip()
c = file.readline().strip()

result = MultipleAlignment(a, b, c)

for r in result:
    print(r)