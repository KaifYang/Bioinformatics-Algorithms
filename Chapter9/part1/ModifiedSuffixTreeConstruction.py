from collections import defaultdict

def ModifiedSuffixTrieConstruction(text):
    degrees = defaultdict(list)
    Trie = defaultdict(list)
    count = 0
    Trie[0] = []
    degrees[0] = [0, 0]

    for i in range(len(text)):
        currentNode = 0

        for j in range(i, len(text)-1):
            currentSymbol = text[j]

            isin = False

            for n in Trie[currentNode]:
                if n[1] == currentSymbol:
                    currentNode = n[0]
                    isin = True
                    break
            
            if not isin:
                count += 1
                Trie[count] = []
                degrees[count] = [1, 0]
                #count is the node the edge is going to, symbol is the char on the edge, j is the position of this edge in text
                Trie[currentNode].append((count, currentSymbol, j))
                degrees[currentNode][1] += 1

                currentNode = count
            
        if len(Trie[currentNode]) == 0:
            Trie[currentNode].append(i)

    return (Trie, degrees)
    

def ModifiedSuffixTreeConstruction(text):
    text = text + '$'
    NBPaths = []
    td = ModifiedSuffixTrieConstruction(text)
    Trie = td[0]
    degrees = td[1]
    delete = []

    for v in Trie:
        #if v is not 1 in 1 out
        if not (degrees[v][0] == 1 and degrees[v][1] == 1):
            #if out degree of v is larger than 1
            if degrees[v][1] > 0:
                #store the edges it needs to add
                changes = []
                #go through all nodes v is connected to
                for edge in Trie[v]:
                    #record the path length and its startpoint
                    start = edge[2]
                    length = 1
                    #get the next node
                    w = edge[0]
                    #if the next node is 1 in 1 out
                    while degrees[w][0] == 1 and degrees[w][1] == 1:
                        #delete the node
                        delete.append(w)

                        u = Trie[w][0]
                        #extend the path length
                        length += 1
                        #proceed to next node
                        w = u[0]
                    #put the result in to changes
                    changes.append((w, start, length))
                #change the edges of node v
                Trie[v] = changes.copy()
                
                #store the nonbranching paths
                for c in changes:
                    NBPaths.append(text[c[1]:(c[1]+c[2])])
    
    for d in delete:
        del Trie[d]

    return (Trie, NBPaths)

file = open('Chapter9\dataset_865524_4.txt')

string = file.readline().strip()

result = ModifiedSuffixTreeConstruction(string)

for r in result[1]:
    print(r, end = ' ')


