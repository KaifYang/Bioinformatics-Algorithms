from collections import defaultdict

def TopologicalOrdering(Graph):
    
    incoming = defaultdict(list)

    for g in Graph:
        for i in Graph[g]:
            incoming[i].append(g)

    l = list()
    Candidates = []

    for n in Graph:
        if n not in incoming:
            Candidates.append(n)

    while not len(Candidates) == 0:
        a = Candidates[0]
        l.append(a)
        Candidates.remove(a)
        
        if a not in Graph:
            continue

        for j in Graph[a]:
            incoming[j].remove(a)
            if len(incoming[j]) == 0:
                Candidates.append(j)
    
    for c in incoming:
        if not len(incoming[c]) == 0:
            return 'the input graph is not a DAG'
    
    return l


file = open('Chapter5(2)\dataset_865456_3.txt')

graph = defaultdict()

while True:
  
    line = file.readline().replace(':', '').split()
  
    if not line:
        break
    
    key = int(line[0])

    values = line[1:]
    values = [int(i) for i in values]

    graph[key] = values

TO = TopologicalOrdering(graph)

for t in TO:
    print(t, end = ' ')