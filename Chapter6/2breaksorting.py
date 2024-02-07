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


def CycleToChromosome(Nodes):
    Chromosome = [0] * (len(Nodes)//2)

    for j in range(1, len(Nodes)//2 + 1):
        if Nodes[(2*j-1) - 1] < Nodes[(2*j) - 1]:
            Chromosome[j - 1] = int(Nodes[(2*j) - 1]/2)

        else:
            Chromosome[j - 1] = -int(Nodes[(2*j-1) - 1]/2)

    return Chromosome



def GraphToGenome(GG:list):
    gg = GG.copy()

    P = []

    #get all possible cycles by looking at the cycle node
    nodeslist = []
    currentcycle = []
    
    current = gg[0]
    
    stack = [gg[0]]

    while not (len(gg) == 0):
        #print('stack:')
        #print(stack)
        
        gg.remove(current)

        if not len(stack) == 1:
            if (stack[0][0] == stack[-1][1]-1 and stack[-1][1]%2 == 0) or (stack[0][0] == stack[-1][1]+1 and stack[-1][1]%2 == 1):
                #print('end')
                nodeslist.append(stack.copy())
                stack.clear()
                if not (len(gg) == 0):
                    stack.append(gg[0])
                    current = gg[0]
                continue

            elif (stack[0][0] == stack[-1][0]-1 and stack[-1][0]%2 == 0) or (stack[0][0] == stack[-1][0]+1 and stack[-1][0]%2 == 1):
                #print('end')
                nodeslist.append(stack.copy())
                stack.clear()
                if not (len(gg) == 0):
                    stack.append(gg[0])
                    current = gg[0]
                continue

        #if the second int in tuple is even, then it is a head
        if stack[-1][1]%2 == 0:
            for g in gg:
                if g[0] == stack[-1][1]-1:
                    stack.append(g)
                    current = g
                    break
                            
                #adjust the node if it is fliped upsidedown
                elif g[1] == stack[-1][1]-1:
                    stack.append((g[1], g[0]))
                    current = g
                    break
                    
        #if the second int in tuple is odd, then it is a tail
        else:
            for g in gg:
                if g[0] == stack[-1][1]+1:
                    stack.append(g)
                    current = g
                    break
                    
                elif g[1] == stack[-1][1]+1:
                    stack.append((g[1], g[0]))
                    current = g
                    break
        

    for n in nodeslist:
        Nodes = []

        for i in range(len(n)):
            #deal with the cycle node
            if i==len(n)-1:
                Nodes.append(n[i][0])
                Nodes.insert(0, n[i][1])

            else:
                Nodes.append(n[i][0])
                Nodes.append(n[i][1])

        Chromosome = CycleToChromosome(Nodes)
        P.append(Chromosome)
    
    return P



def TwoBreak(GG: list, i1, i2, i3, i4):

    gg = GG.copy()
    
    breakset = []

    for g in gg:
        if g == (i1, i2) or g == (i2, i1):
            breakset.append(g)
        if g == (i3, i4) or g == (i4, i3):
            breakset.append(g)

    for b in breakset:
        gg.remove(b)

    gg.append((i1, i3))
    gg.append((i2, i4))


    return gg



def TwoBreakOnGenome(P, i1, i2, i3, i4):

    Pedges = ColoredEdges(P)

    GenomeGraph = TwoBreak(Pedges, i1, i2, i3, i4)
    
    P = GraphToGenome(GenomeGraph)

    return P


def TwoBreakSorting(P, Q):

    steps = [P.copy()]

    RedEdges = ColoredEdges(P)
    BlueEdges = ColoredEdges(Q)

    BreakPointGraph = defaultdict(list)

    for r in RedEdges:
        BreakPointGraph[r[0]].append(r[1])
        BreakPointGraph[r[1]].append(r[0])
    
    for b in BlueEdges:
        BreakPointGraph[b[0]].append(b[1])
        BreakPointGraph[b[1]].append(b[0])
    
    distance = TwoBreakDistance(P, Q)

    #for each blue edge, if we do not see the same edge twice in the graph, we do the operation
    for b in BlueEdges:
        #do two break on the blue edge if it does not have self cycle
        if not BreakPointGraph[b[0]].count(b[1]) == 2:
            i1 = b[0]
            for i in BreakPointGraph[b[0]]:
                if not (i == b[1]):
                    i2 = i
                    break
            i3 = b[1]
            for j in BreakPointGraph[b[1]]:
                if not (j == b[0]):
                    i4 = j
                    break
            
            BreakPointGraph[i1].remove(i2)
            BreakPointGraph[i2].remove(i1)
            BreakPointGraph[i3].remove(i4)
            BreakPointGraph[i4].remove(i3)

            BreakPointGraph[i1].append(i3)
            BreakPointGraph[i3].append(i1)
            BreakPointGraph[i2].append(i4)
            BreakPointGraph[i4].append(i2)

            p = TwoBreakOnGenome(steps[-1], i1, i2, i3, i4)
            steps.append(p)

    return steps



#file = open('Chapter6\dataset_865469_4.txt')

#sp = file.readline().strip()
sp = '(+5 +11 -7 -12 +13 +2 +9 -14 +15 +3 -8 -10 +1 -6 -4)'
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

#sq = file.readline().strip()
sq = '(+2 -7 +4 +3 +5 -10 +9 +6 +12 -14 +15 -8 +13 +11 +1)'
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

result = TwoBreakSorting(P, Q)

for r in result:
    for b in r:
        print('(', end = '')
        for a in range(len(b)):
            if b[a] > 0:
                print('+' + str(b[a]), end = '')
            else:
                print(str(b[a]), end = '')
            
            if a == len(b)-1:
                continue
            else:
                print(' ', end = '')
        print(')', end = '')

    print('\n')
        
        