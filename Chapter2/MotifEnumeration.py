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


def ApproximatePatternExist(Pattern: str, Text: str, d: int):
    l = len(Pattern)

    for i in range(0, len(Text)-l+1):
        mis = HammingDistance(Text[i:i+l], Pattern)
        if mis <= d:
            return True
    
    return False
    
    



def MotifEnumeration(Dna, k, d):
    Patterns = set()

    Pt = set()

    for s in Dna:
        for j in range(0, len(s)-k+1):
            Patt = s[j:j+k]
            if Patt not in Pt:
                Pt.add(Patt)

    for i in Pt:
        nbh = Neighbors(i, d)
        
        for n in nbh:

            exist = True

            for a in Dna:
                if not ApproximatePatternExist(n, a, d):
                    exist = False

            if exist:
                if n not in Patterns:
                    Patterns.add(n)

    return Patterns


Dna = {'GGGGTGGAAGGACCTCATCAGGTTA', 'TTTTGTCATTGCGGTGGTTATACCC', 'GCGAAAGTTATAGTTGCCTCCCGTG', 'GCTGGGCCCCCGTTATACGGCAATG', 'TACTTACTGCAAGGCAGGGGTGTTA', 'TTTCTTTCAATGCGCCGTTAACGCC'}
k = 5
d = 1

result = MotifEnumeration(Dna, k ,d)

for r in result:
    print(r, end=' ')