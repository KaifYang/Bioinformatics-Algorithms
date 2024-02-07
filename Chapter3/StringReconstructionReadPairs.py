from collections import defaultdict

def DeBruijnKmers(kmers: list[tuple()]):
    graph = defaultdict(list)

    for k in kmers:
        prefix1 = k[0][:-1]
        prefix2 = k[1][:-1]
        suffix1 = k[0][1:]
        suffix2 = k[1][1:]

        graph[(prefix1, prefix2)].append((suffix1, suffix2))
    
    return graph



def adjustcycle(cycle: list, start):

    ind = cycle.index(start)

    newcycle = [*cycle[ind:], *cycle[:ind]]
    newcycle.append(start)

    return newcycle



def EulerianCycle(G: dict):
    
    haveedges = []
    
    for key in G:
        start = key
        break 
    
    current = G[start].pop(0)

    if len(G[start]) > 0:
        haveedges.append(start)

    cycle = [start]

    
    while True:

        if not current == start:

            #update cycle
            cycle.append(current)
            
            #get next node
            next = G[current].pop(0)

            #print(str(current) + ' c')
            #print(next)

            #check if current node still have edges and update haveedges if necessary
            if current not in haveedges:
                if len(G[current]) > 0:
                    haveedges.append(current)
            
            else:
                if len(G[current]) == 0:
                    haveedges.remove(current)

            #go next
            current = next

        
        else:
            #check if we get the result
            if len(haveedges) == 0:
                cycle.append(start)
                return cycle

            #get the node in the cycle that still have edges
            start = haveedges[0]
            
            #adjust the cycle to start and end at the start node
            cycle = adjustcycle(cycle, start)

            #go next
            #print(G[start])
            current = G[start].pop(0)

            #remove the node if it does not have any edges going out
            if len(G[start]) == 0:
                haveedges.remove(start)



def EulerianPath(G: dict[int, list[int]]):
    lackin = ''
    lackout = ''

    count = defaultdict()

    for k in G:
        count[k] = [0, 0]

    #add the missing nodes to the graph
    missing = []

    for ke in G:
        for j in G[ke]:
            if j not in G:
                missing.append(j)

    for m in missing:
        G[m] = []
        count[m] = [0, 0]


    for key in G:

        #record the count of edges going out
        count[key][0] = len(G[key])

        #record the count of edges going in
        for i in G[key]:
            count[i][1] += 1

    
    for c in count:
        if count[c][0] < count[c][1]:
            lackout = c
        elif count[c][0] > count[c][1]:
            lackin = c

    G[lackout].append(lackin)

    cycle = EulerianCycle(G)

    path = cycle[:-1]

    for i in range(len(path)-1):
        if path[i] == lackout and path[i+1] == lackin: 
            path = [*path[i+1:], *path[:i+1]]

    return path



def GenomePath(path):
    string = ''
    for p in path:
        if string == '':
            string = string + p
        else:
            string = string + p[-1]
    
    return string


def GappedGenomePath(Patterns, k ,d):
    FirstPatterns = []
    SecondPatterns = []

    for p in Patterns:
        FirstPatterns.append(p[0])
        SecondPatterns.append(p[1])

    prefix = GenomePath(FirstPatterns)
    suffix = GenomePath(SecondPatterns)

    for i in range(k+d, len(prefix)):
        if not prefix[i:i+1] == suffix[i-k-d:i-k-d+1]:
            return 'there is no string spelled by the gapped patterns'
    
    return prefix + suffix[-k-d:]



def StringReconstructionReadPairs(Patterns: list[str], k: int, d: int):
    dB = DeBruijnKmers(Patterns)
    path = EulerianPath(dB)
    Text = GappedGenomePath(path, k, d)

    return Text


file = open('dataset_865404_16.txt')

file.readline()

string = file.readline().strip()

string = string.split()

pairs = []

for s in string:
    a = s.replace('|', ' ').split()

    pairs.append((a[0], a[1]))

k = 50
d = 200

print(StringReconstructionReadPairs(pairs, k ,d))