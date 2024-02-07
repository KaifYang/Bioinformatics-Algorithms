from collections import defaultdict
import itertools

def DeBruijnKmers(kmers: list[str]):
    graph = defaultdict(list)

    for k in kmers:
        prefix = k[:-1]
        suffix = k[1:]

        graph[prefix].append(suffix)
    
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



def GenomePath(path):
    string = ''
    for p in path:
        string = string + p[0]
    
    return string

def StringReconstruction(k: int):
    bkmerstuple = list(itertools.product(['0', '1'], repeat=k)) 
    bkmerslist = []
    for b in bkmerstuple:
        kmer = ''
        for a in b:
            kmer += a
        bkmerslist.append(kmer)
    
    dB = DeBruijnKmers(bkmerslist)
    cycle = EulerianCycle(dB)
    cycle = cycle[:-1]
    Text = GenomePath(cycle)

    return Text

print(StringReconstruction(9))