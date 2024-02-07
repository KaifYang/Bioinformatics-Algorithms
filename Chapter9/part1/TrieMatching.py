
from collections import defaultdict

def TrieConstruction(Patterns):

    Trie = defaultdict(list)

    count = 0

    Trie[0] = []
    for p in Patterns:
        currentNode = 0

        for i in range(len(p)):

            currentSymbol = p[i]

            isin = False

            for n in Trie[currentNode]:
                if n[1] == currentSymbol:
                    currentNode = n[0]
                    isin = True
                    break
            
            if not isin:
                count += 1
                Trie[count] = []
                Trie[currentNode].append((count, currentSymbol))
                currentNode = count

    return Trie


def PrefixTrieMatching(Trie, text):
    symbol = text[0]
    posi = 0

    v = 0
    pattern = ''

    while True:

        isin = False

        for t in Trie[v]:
            if t[1] == symbol:
                isin = True
                edge = t
                break

        if len(Trie[v]) == 0:
            return pattern
        
        elif isin:
            v = edge[0]
            pattern += edge[1]
            posi += 1

            if len(Trie[v]) == 0:
                return pattern

            if posi > len(text)-1:
                return 'no'

            symbol = text[posi]
            

        else:
            return 'no'



def TrieMatching(patt, text):
    Trie = TrieConstruction(patt)

    positions = defaultdict(list)

    posi = 0

    while not len(text) == 0:
        pattern = PrefixTrieMatching(Trie, text)

        if not pattern == 'no':
            positions[pattern].append(posi)

        text = text[1:]
        posi += 1
    
    return positions

file = open('Chapter9\dataset_865522_8.txt')
text = file.readline().strip()
patterns = file.readline().strip()
patterns = patterns.split()

result = TrieMatching(patterns, text)

for r in result:
    print(r, end = ': ')

    for i in result[r]:
        print(i, end = ' ')

    print('')