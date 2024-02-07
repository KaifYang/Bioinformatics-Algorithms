from collections import defaultdict

def Viterbi(string, char:list, states, transition, emission):
    graph = defaultdict()
    predecessor = defaultdict()

    source = 1

    for sidx, s in enumerate(states):
        startidx = char.index(string[0])
        weight = (1/len(states)) * emission[sidx][startidx]
        graph[(s, 0)] = source * weight
        predecessor[(s, 0)] = 'source'

    for i in range(1, len(string)):
        symbol = string[i]
        symbolidx = char.index(symbol)

        for stateidx, currs in enumerate(states):

            maxpr = 0    
            
            for previdx, prevs in enumerate(states):

                currpr = graph[(prevs, i-1)] * transition[previdx][stateidx] * emission[stateidx][symbolidx]

                if currpr > maxpr:
                    maxpr = currpr
                    predecessor[(currs, i)] = (prevs, i-1)
            
            graph[(currs, i)] = maxpr

    maxprobability = max([graph[(st, len(string)-1)] for st in states])

    for sta in states:
        if graph[(sta, len(string)-1)] == maxprobability:
            last = (sta, len(string)-1)
    
    hiddenpath = ''

    while not last == 'source':
        hiddenpath = last[0] + hiddenpath
        last = predecessor[last]
    
    return hiddenpath

file = open('Chapter10\dataset_865547_7.txt')

lines = file.read().splitlines()

string = lines[0].strip()

char = lines[2].strip().split() 

states = lines[4].strip().split() 

transition = []
emission = []

for idx, line in enumerate(lines):

    if idx <= 6:
        continue
    
    if '-' in line:
        stop = idx
        break

    transition.append([float(x) for x in line.split()[1:].copy()])

for l in range(stop+2, len(lines)):
    emission.append([float(x) for x in lines[l].split()[1:].copy()])

print(Viterbi(string, char, states, transition, emission))
    