from collections import defaultdict

def ChromosomeToCycle(Chromosome):
    Nodes = [None] * (len(Chromosome)*2)
    
    #j is the index on the chromosome
    for j in range(1, len(Chromosome)+1):
        i = Chromosome[j-1]

        if i > 0:
            Nodes[(2*j-1) - 1] = 2*i - 1
            Nodes[(2*j) - 1] = 2*i
        
        #since i < 0 we need to reverse its sign to make the indexing work
        else:
            Nodes[(2*j-1) - 1] = -(2*i)
            Nodes[(2*j) - 1] = -(2*i) - 1
    
    return Nodes 

def ColoredEdges(P):
    edges = []

    for chr in P:
        Nodes = ChromosomeToCycle(chr)
        
        for j in range(1, len(chr)+1):
            if j == len(chr):
                edges.append((Nodes[(2*j) - 1], Nodes[0]))
            else:
                edges.append((Nodes[(2*j) - 1], Nodes[(2*j+1) - 1]))
    
    return edges
    
def TwoBreakDistance(P, Q):

    edges = defaultdict(list)

    Pedges = ColoredEdges(P)

    qq = len(Pedges)

    Qedges = ColoredEdges(Q)
    
    for p in Pedges:
        edges[p[0]].append(p[1])
        edges[p[1]].append(p[0])

    for q in Qedges:
        edges[q[0]].append(q[1])
        edges[q[1]].append(q[0])

    cyclecount = 0
    stack = []
    visited = set()

    while not len(edges)==0:
        for e in edges:
            start = e
            break

        stack.append(start)

        while not len(stack)==0:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)

            for c in edges[current]:
                stack.insert(0, c)

            del edges[current]
            
        cyclecount += 1

    return qq - cyclecount

file = open('Chapter6\dataset_865469_4.txt')

sp = file.readline().strip()
#sp = '(+1 +2 +3 +4 +5 +6)'
stringp = sp.split(')(')

#remove extra braket
for i in range(len(stringp)):
    if stringp[i][0] == '(':
        stringp[i] = stringp[i][1:]
    
    if stringp[i][-1] == ')':
        stringp[i] = stringp[i][:-1]

P = []

for t in stringp:
    chr = t.split()
    chr = [int(a) for a in chr]

    P.append(chr)

sq = file.readline().strip()
#sq = '(+1 -3 -6 -5)(+2 -4)'
stringq = sq.split(')(')

#remove extra braket
for j in range(len(stringq)):
    if stringq[j][0] == '(':
        stringq[j] = stringq[j][1:]
    
    if stringq[j][-1] == ')':
        stringq[j] = stringq[j][:-1]

Q = []

for s in stringq:
    chr = s.split()
    chr = [int(b) for b in chr]

    Q.append(chr)

print(TwoBreakDistance(P, Q))

