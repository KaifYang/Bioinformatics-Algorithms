def HammingDistance(one: str, two: str):

    mismatch = 0

    for i in range(0, len(one)):
        if not one[i:i+1] == two[i:i+1]:
            mismatch += 1

    return mismatch

def ApproximatePatternCount(Pattern: str, Text: str, d: int):
    count = 0
    
    for i in range(0, len(Text)-len(Pattern)+1):
        Pt = Text[i:i+len(Pattern)]
        if HammingDistance(Pattern, Pt) <= d:
            count = count + 1

    return count


print(ApproximatePatternCount('TTCAC', 'TTTGGGGACGTCGGAGGGGGGATTAATCGTATATTACCAGGGAGAAGATAGATAGGAAGGTCGCAGTTCGTTCTGTGGATCAGCTACTTAGAGAGCATATTAAGAGGGTTTTTACAAAGTAGCTAATTCGCCAACCCGAGGTTGGGACTGATTGACAACGTCAGTGCAGAGATGGTTCGGGCATTAACGTTCTGAAAGATCATAGCCCGCCCGGGCTTCCACTTTCACGGTATCCTATTCAGGGGAAGAGGGTGCTCGACTTAGTAGCCGCGTGGGCTATTGGGATCTTATTTGGCTCTTGTG', 3))