from collections import defaultdict

def LongestPath(s: int, t: int, E: dict[int, list[tuple[int, int]]]) -> tuple[int, list[int]]:

    previous = defaultdict(list)
    weight = dict()
    predecessor = dict()

    for e in E:
        for i in E[e]:
            next = i[0]
            w = i[1]
            previous[next].append((e, w))

    for b in previous:
        if b not in E:
            E[b] = []

    sortedE = dict(sorted(E.items()))
    print(sortedE)
    #loop through the nodes in topological order
    for a in sortedE:
        #if the node has no edge coming in its weight is 0
        if a not in previous:
            weight[a] = 0
            continue
        
        max = float('-inf')

        #loop through all the previous nodes
        for p in previous[a]:
            
            pre = p[0]
            wei = p[1]
            
            if weight[pre] + wei > max:
                #update max weight
                max = weight[pre] + wei
                #update predecessor node
                predecessor[a] = pre
        
        weight[a] = max

    path = list()
    
    length = weight[t] - weight[s]

    current = t

    while not current == s:
        path.insert(0, current)
        current = predecessor[current]
    
    path.insert(0, current)

    result = (length, path)

    return result

file = open('Chapter4\dataset_865447_7.txt')
st = file.readline().strip().split()
s = int(st[0])
t = int(st[1])

E = defaultdict(list)

line = file.readline().strip().split()


while line:
    E[int(line[0])].append((int(line[1]), int(line[2])))
    line = file.readline().strip().split()
    

result = LongestPath(s, t, E)

print(result[0])

for r in result[1]:
    print(r, end = ' ')