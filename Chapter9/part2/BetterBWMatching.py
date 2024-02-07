from collections import defaultdict

def BetterBWMatching(text, Patterns):
    #record the count matrix. Where stores the position of char on the countmatrix and positions of its different occurences in the BWT
    where = defaultdict()
    wherecount = 0
    countmatrix = []
    #get first column and last column of M
    Last = [*text]
    First = Last.copy()
    First.sort()

    FirstOccur = []

    for f in range(len(First)):
        #record the sequence of the chars in the countmatrix
        if First[f] not in where:
            FirstOccur.append(f)
            where[First[f]] = wherecount
            wherecount += 1  

    #print(where)
    #print(FirstOccur)

    #initialize countmatrix
    firstrow = [0]*len(where)
    countmatrix.append(firstrow)

    for l in Last:
        #update countmatrix
        index = where[l]
        row = list(countmatrix[-1]).copy()
        row[index] = row[index] + 1
        countmatrix.append(row.copy())


    positions = []

    for pattern in Patterns:
        top = 0
        bottom = len(Last)-1

        while top <= bottom:
            if len(pattern) > 0:
                symbol = pattern[-1]
                #print(symbol)
                ind = where[symbol]
                pattern = pattern[:-1]

                topnum = countmatrix[top][ind] 
                bottomnum = countmatrix[bottom+1][ind]

                #print(topnum, end = ' ')
                #print(bottomnum)

                top = FirstOccur[ind] + topnum
                bottom = FirstOccur[ind] + bottomnum - 1

                if top > bottom:
                    positions.append(0)
                    break
                
                #print(top, end = ' ')
                #print(bottom)

            #if found the match
            else:
                #print(top, end = ' ')
                #print(bottom)

                positions.append(bottom - top + 1)
                break
    
    return positions

file = open('Chapter9(2)\dataset_865530_7.txt')

text = file.readline().strip()
Patterns = file.readline().strip()

Patterns = Patterns.split()

result = BetterBWMatching(text, Patterns)

for r in result:
    print(r, end = ' ')