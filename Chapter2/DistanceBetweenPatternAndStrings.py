
def HammingDistance(one: str, two: str):

    mismatch = 0

    for i in range(0, len(one)):
        if not one[i:i+1] == two[i:i+1]:
            mismatch += 1

    return mismatch




def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0

    for txt in Dna:
        HD = float('inf')

        for i in range(0, len(txt)-k):
            pt = txt[i:i+k]
            hd = HammingDistance(Pattern, pt)
            if HD > hd:
                HD = hd

        distance = distance + HD
    
    return distance


file = open('Chapter2\dataset_865389_1.txt')

patt = file.readline().strip()

dna = file.readline().strip().split()

print(DistanceBetweenPatternAndStrings(patt, dna))


