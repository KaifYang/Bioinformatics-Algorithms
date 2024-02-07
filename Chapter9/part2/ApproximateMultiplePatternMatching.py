from collections import defaultdict

#this algorithm needs recursion

def BurrowsWheelerTransform(text):
    text = text + '$'
    #get all cyclic rotation of the text
    rotations = []

    for i in range(len(text)):
        rotations.append(text[-i:] + text[:-i])
    
    #print(rotations)

    rotations.sort()

    BWT = ''

    for r in rotations:
        BWT += r[-1]

    return BWT


def findnum(partialarrays, posi, ind, C, Last, symbol):
    above = posi//C

    #print(above, end = ' ')
    #print(posi)

    startnum = partialarrays[above][ind]

    #print(startnum, end = ' ')

    for i in range(above*C, posi):
        if Last[i] == symbol:
            startnum += 1
    
    #print(startnum)

    return startnum


def recursivefindposi(partialarrays, psa:list, Last, positions:defaultdict, where, C, FirstOccur, top, bottom, pattern, currpatt, d, currd):
    #print('currpatt: ' + currpatt)
    #print(currd, end = ' ')
    #print(d)
    
    if len(currpatt) > 0:

        if currd == d:
            symbol = currpatt[-1]
            #print(symbol)
            if symbol not in where:
                return
            
            topnum = findnum(partialarrays, top, where[symbol], C, Last, symbol)
            bottomnum = findnum(partialarrays, bottom+1, where[symbol], C, Last, symbol)

            top = FirstOccur[where[symbol]] + topnum
            bottom = FirstOccur[where[symbol]] + bottomnum - 1
            
            #print(top, end = ' ')
            #print(bottom)

            if top > bottom:
                return

            recursivefindposi(partialarrays, psa, Last, positions, where, C, FirstOccur, top, bottom, pattern, currpatt[:-1], d, currd)
        
        else:
            for w in where:
                if w == '$':
                    continue
                symbol = w
                #print(symbol)
                topnum = findnum(partialarrays, top, where[symbol], C, Last, symbol)
                bottomnum = findnum(partialarrays, bottom+1, where[symbol], C, Last, symbol)

                wtop = FirstOccur[where[symbol]] + topnum
                wbottom = FirstOccur[where[symbol]] + bottomnum - 1

                #print(top, end = ' ')
                #print(bottom)

                if top > bottom:
                    return

                if symbol == currpatt[-1]:    
                    recursivefindposi(partialarrays, psa, Last, positions, where, C, FirstOccur, wtop, wbottom, pattern, currpatt[:-1], d, currd)
                else:
                    recursivefindposi(partialarrays, psa, Last, positions, where, C, FirstOccur, wtop, wbottom, pattern, currpatt[:-1], d, currd+1)

    else:
        #print('end')
        for e in range(top, bottom+1):
            index = e
            count = 0
            while not index in psa:
                lastsymbol = Last[index]

                index = findnum(partialarrays, index, where[lastsymbol], C, Last, lastsymbol)
                index = FirstOccur[where[lastsymbol]] + index
                count += 1

            posi = psa.index(index)*C + count

            #print(posi)

            positions[pattern].append(posi)
        


#only save part of the countmatrix, track backward 

def BetterBWMatching(text, Patterns, C, d):
    text = BurrowsWheelerTransform(text)
    #record the count matrix. Where stores the position of char on the countmatrix 
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

    del First

    #print(where)
    #print(FirstOccur)

    #initialize countmatrix
    count = [0]*len(where)
    
    for l in range(len(Last)+1):

        if l%C == 0:
            countmatrix.append(count.copy())

        if l == len(Last):
                break

        #update countmatrix
        index = where[Last[l]]
        count[index] = count[index] + 1


    #build partial suffix array
    psa = list([None] * ((len(Last)-1)//C + 1))
    place = 0
    entry = len(Last)-1

    while None in psa:
        #print(place, end = ' ')
        #print(entry)
        if entry%C == 0:
            psa[entry//C] = place

        endsymbol = Last[place]
        place = findnum(countmatrix, place, where[endsymbol], C, Last, endsymbol)
        place = FirstOccur[where[endsymbol]] + place
        entry -= 1

    positions = defaultdict(list)

    for pattern in Patterns:
        
        recursivefindposi(countmatrix, psa, Last, positions, where, C, FirstOccur, 0, len(Last)-1, pattern, pattern, d, 0)
        
        if pattern not in positions:
            positions[pattern] = []

    return positions

file = open('Chapter9(2)\dataset_865533_10.txt')

text = file.readline().strip()
Patterns = file.readline().strip()
d = int(file.readline().strip())
#text = 'ACATGCTACTTT'
#Patterns = 'ATT GCC GCTA TATT'
#text = 'panamabananas'
#Patterns = 'ana'
#d = 1
Patterns = Patterns.split()

#file.close()

out = open('answer.txt', 'w')

result = BetterBWMatching(text, Patterns, 5, d)

for r in result:
    if len(result[r]) == 0:
        out.write(r + ': ')
        out.write('\n')
        continue
    
    else :
        out.write(r + ': ')

    for a in range(len(result[r])):

        if a == len(result[r])-1:
            out.write(str(result[r][a]) + '\n')

        else:
            out.write(str(result[r][a]) + ' ')
    