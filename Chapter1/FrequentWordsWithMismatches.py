
def HammingDistance(one: str, two: str):

    mismatch = 0

    for i in range(0, len(one)):
        if not one[i:i+1] == two[i:i+1]:
            mismatch += 1

    return mismatch



def Neighbors(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {'A', 'T', 'C', 'G'}

    nbh = set()
    suffixnbh = Neighbors(Pattern[1:], d)

    for i in suffixnbh:
        if HammingDistance(Pattern[1:], i) < d:
            nbh.add('A' + i)
            nbh.add('T' + i)
            nbh.add('C' + i)
            nbh.add('G' + i)
        else:
            nbh.add(Pattern[0:1] + i)
    
    return nbh



def MaxMap(map):
    max = float('-inf')

    for key in map:
        if map[key] > max:
            max = map[key]
    
    return max




def FrequentWordsWithMismatches(Text: str, k: int, d:int):
    Patterns = []
    freqMap = {}
    n = len(Text)

    for i in range(0, n-k+1):
        Pattern = Text[i:i+k]
        nbh = Neighbors(Pattern, d)

        for j in nbh:
            if not j in freqMap:
                freqMap[j] = 1
            else:
                freqMap[j] += 1
    
    m = MaxMap(freqMap)

    for key in freqMap:
        if freqMap[key] == m:
            Patterns.append(key)

    return Patterns

file = open('dataset_865367_9.txt')

txt = file.readline().strip()
k = 5
d = 2

fwm = FrequentWordsWithMismatches(txt, k, d)

for f in fwm:
    print(f, end=' ')