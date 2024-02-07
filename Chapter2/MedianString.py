
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




def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0

    for txt in Dna:
        HD = float('inf')

        #find the substring that has the smallest hammingdistance with Pattern
        for i in range(0, len(txt)-k):
            pt = txt[i:i+k]
            hd = HammingDistance(Pattern, pt)
            if HD > hd:
                HD = hd

        distance = distance + HD
    
    return distance


#O(4^k · n · k · t)

def MedianString(k, Dna):
    distance = float('inf')

    Sample = ''
    for q in range(0, k):
        Sample = Sample + 'A'

    #get all Patterns with length of k
    Patterns = Neighbors(Sample, k)


    for p in Patterns:
        d = DistanceBetweenPatternAndStrings(p, Dna)
        if distance > d:
            distance = d
            Median = p
    
    return Median

file = open('Chapter2\dataset_865381_9.txt')

patt = int(file.readline().strip())

dna = file.readline().strip().split()

print(MedianString(patt, dna))




