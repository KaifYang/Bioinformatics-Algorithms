# find the two node with unbalanced number of edges and connect them then run EulerianPath algorithm then delete the extra node at the end
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


file = open('dataset_865403_6.txt')

graph = defaultdict()

while True:
  
    line = file.readline().replace(':', '').split()
  
    if not line:
        break
    
    key = int(line[0])

    values = line[1:]
    values = [int(i) for i in values]

    graph[key] = values

path = EulerianPath(graph)

for c in path:
    print(c, end = ' ')