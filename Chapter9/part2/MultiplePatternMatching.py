from collections import defaultdict

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


#get all the suffix of the text and sort them 
def PartialSuffixArray(text, C):
    suffixes = []
    count = 0
    for i in range(len(text)):
        suffixes.append((text[i:], count))
        count += 1
    
    suffixes.sort()

    length = len(suffixes) // C

    lis = [None] * length

    print(suffixes)
    print(lis)

    for s in range(len(suffixes)):
        posi = suffixes[s][1]

        if posi%C == 0:
            lis[posi//C] = s

    return lis


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


#only save part of the countmatrix, track backward 

def BetterBWMatching(text, Patterns, C):
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
        top = 0
        bottom = len(Last)-1
        patt = pattern

        while top <= bottom:
            if len(patt) > 0:
                symbol = patt[-1]
                #print(symbol)
                if symbol not in where:
                    break

                ind = where[symbol]
                patt = patt[:-1]

                topnum = findnum(countmatrix, top, ind, C, Last, symbol)
                bottomnum = findnum(countmatrix, bottom+1, ind, C, Last, symbol)

                #print(topnum, end = ' ')
                #print(bottomnum)

                top = FirstOccur[ind] + topnum
                bottom = FirstOccur[ind] + bottomnum - 1
                
                #print(top, end = ' ')
                #print(bottom)

            #if found the match
            else:
                #print(top, end = ' ')
                #print(bottom)
                #print(psa)

                #get positions of the repeats
                for d in range(top, bottom+1):
                    index = d
                    count = 0
                    while not index in psa:
                        lastsymbol = Last[index]

                        #print(lastsymbol)

                        index = findnum(countmatrix, index, where[lastsymbol], C, Last, lastsymbol)
                        index = FirstOccur[where[lastsymbol]] + index
                        count += 1

                    posi = psa.index(index)*C + count

                    #print(index)

                    positions[pattern].append(posi)

                break
        
        if pattern not in positions:
            positions[pattern] = []

    return positions

file = open('')
text = file.readline().strip()
Patterns = file.readline().strip()
#text = 'ATATATATAT'
#Patterns = 'GT AGCT TAA AAT AATAT'
Patterns = Patterns.split()

result = BetterBWMatching(text, Patterns, 10)

for r in result:
    if len(result[r]) == 0:
        print(r + ': ')
    
    else :
        print(r, end = ': ')

    for a in range(len(result[r])):

        if a == len(result[r])-1:
            print(result[r][a])

        else:
            print(result[r][a], end = ' ')
    
