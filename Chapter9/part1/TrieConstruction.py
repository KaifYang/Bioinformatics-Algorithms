from collections import defaultdict

def TrieConstruction(Patterns, file):

    ans = open(file, 'w')

    Trie = defaultdict(list)

    count = 0

    Trie[0] = []
    for p in Patterns:
        currentNode = 0

        for i in range(len(p)):

            currentSymbol = p[i]

            isin = False

            for n in Trie[currentNode]:
                if n[2] == currentSymbol:
                    currentNode = n[1]
                    isin = True
                    break
            
            if not isin:
                count += 1
                Trie[count] = []
                Trie[currentNode].append((currentNode, count, currentSymbol))
                currN = str(currentNode)
                cc = str(count)
                ans.write(currN + ' ' + cc + ' ' + currentSymbol + '\n')
                currentNode = count

    return Trie

file = open('Chapter9\dataset_865522_4.txt')

l = file.readline().strip().split()

file.close()

TrieConstruction(l, 'answer')