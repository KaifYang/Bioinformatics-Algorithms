from collections import defaultdict

def inverseBWT(text):
    #get first column and last column of M
    Last = [*text]
    First = Last.copy()
    First.sort()
    
    id = defaultdict()
    for l in Last:
        if l not in id:
            id[l] = 1     

    newFirst = []

    for f in First:
        newFirst.append((f, id[f]))
        id[f] += 1

    #reset id
    for d in id:
        id[d] = 1

    newLast = []

    for l in Last:
        newLast.append((l, id[l]))
        id[l] += 1

    origin = [newFirst[0]]

    for i in range(len(newLast)-1):
        endchar = origin[-1]
        for j in range(len(newLast)):
            if newLast[j][0] == endchar[0] and newLast[j][1] == endchar[1]:
                origin.append(newFirst[j])

    string = ''
    for o in origin:
        string += o[0]

    string = string[1:] + string[0]

    return string

#file = open('Chapter9\dataset_865528_11.txt')

#string = file.readline().strip()
string = 'TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC'
print(inverseBWT(string))
