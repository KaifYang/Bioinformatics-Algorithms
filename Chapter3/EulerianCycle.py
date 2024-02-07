from collections import defaultdict

def adjustcycle(cycle: list, start):

    ind = cycle.index(start)

    newcycle = [*cycle[ind:], *cycle[:ind]]
    newcycle.append(start)

    return newcycle



def EulerianCycle(G: dict):
    
    size = len(G)

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

file = open('dataset_865403_2.txt')

graph = defaultdict()

while True:
  
    line = file.readline().replace(':', '').split()
  
    if not line:
        break
    
    key = int(line[0])

    values = line[1:]
    values = [int(i) for i in values]

    graph[key] = values

cycle = EulerianCycle(graph)

for c in cycle:
    print(c, end = ' ')