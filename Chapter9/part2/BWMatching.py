from collections import defaultdict

def BWMatching(text, Patterns):
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

    #get LastToFirst
    LastToFirst = []

    for i in range(len(newLast)):
        for j in range(len(newFirst)):
            if newFirst[j] == newLast[i]:
                LastToFirst.append(j)
    
    positions = []

    for pattern in Patterns:
        top = 0
        bottom = len(Last)-1

        while top <= bottom:
            if len(pattern) > 0:
                symbol = pattern[-1]
                pattern = pattern[:-1]

                topindex = None
                bottomindex = None
                for a in range(top, bottom+1):
                    if Last[a] == symbol:
                        if topindex == None:
                            topindex = a
                        bottomindex = a
                
                #if there is no match
                if (topindex == None and bottomindex == None):
                    positions.append(0)
                    break
                
                top = LastToFirst[topindex]
                bottom = LastToFirst[bottomindex]

            #if found the match
            else:
                positions.append(bottom - top + 1)
                break
    
    return positions

#file = open('Chapter9(2)\dataset_865530_7.txt')

#text = file.readline().strip()
#Patterns = file.readline().strip()
text = 'smnpbnnaaaaa$a'
Patterns = 'ana'
Patterns = Patterns.split()

result = BWMatching(text, Patterns)

for r in result:
    print(r, end = ' ')