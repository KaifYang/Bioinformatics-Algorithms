
import random


def ProfileMostProbableKmer(Text: str, k: int, Profile):
    
    maxpr = float('-inf')
    maxkmer = ''

    for i in range(0, len(Text)-k+1):
        patt = Text[i:i+k]

        pr = 1

        for j in range(0, len(patt)):
            if patt[j:j+1] == 'A':
                pr = pr*Profile[0][j]
            
            elif patt[j:j+1] == 'C':
                pr = pr*Profile[1][j]
            
            elif patt[j:j+1] == 'G':
                pr = pr*Profile[2][j]
            
            elif patt[j:j+1] == 'T':
                pr = pr*Profile[3][j]

        if pr > maxpr:
            
            maxpr = pr
            maxkmer = patt


    return maxkmer


def getProfile(Motifs):
    profile = [[None for y in range(len(Motifs[0]))] for x in range(4)]

    for i in range(len(Motifs[0])):
        Acount = 0.1
        Ccount = 0.1
        Gcount = 0.1
        Tcount = 0.1

        for m in Motifs:
            if m[i:i+1] == 'A':
                Acount += 1
            elif m[i:i+1] == 'C':
                Ccount += 1
            elif m[i:i+1] == 'G':
                Gcount += 1
            elif m[i:i+1] == 'T':
                Tcount += 1
        
        sum = Acount + Ccount + Gcount + Tcount

        profile[0][i] = Acount/sum
        profile[1][i] = Ccount/sum
        profile[2][i] = Gcount/sum
        profile[3][i] = Tcount/sum

    return profile


def HammingDistance(one: str, two: str):

    mismatch = 0

    for i in range(0, len(one)):
        if not one[i:i+1] == two[i:i+1]:
            mismatch += 1

    return mismatch


def getConcensus(Motifs):
    concensus = ''

    profile = getProfile(Motifs)

    for i in range(len(Motifs[0])):
        if profile[0][i] == max(profile[0][i], profile[1][i], profile[2][i], profile[3][i]):
            concensus = concensus + 'A'
        
        elif profile[1][i] == max(profile[0][i], profile[1][i], profile[2][i], profile[3][i]):
            concensus = concensus + 'C'
        
        elif profile[2][i] == max(profile[0][i], profile[1][i], profile[2][i], profile[3][i]):
            concensus = concensus + 'G'
        
        elif profile[3][i] == max(profile[0][i], profile[1][i], profile[2][i], profile[3][i]):
            concensus = concensus + 'T'
    
    return concensus


def getScore(Motifs):
    Score = 0
    concensus = getConcensus(Motifs)
    
    for m in Motifs:
        d = HammingDistance(m, concensus)
        Score += d
    
    return Score



def RandomizedMotifSearch(Dna, k, t):
    
    RMotifs = []
    for i in range(t):
        num = random.randint(0, len(Dna[i])-k)
        RMotifs.append(Dna[i][num:num+k])
        
    BestMotifs = RMotifs


    while True:
        profile = getProfile(BestMotifs)
        Motifs = []
        for j in range(0, t):
            Motifj = ProfileMostProbableKmer(Dna[j], k, profile)
            Motifs.append(Motifj)

        if getScore(Motifs) < getScore(BestMotifs):
            BestMotifs = Motifs
        else:
            return BestMotifs

    


string = 'GCGTAGGGCTCTGTGGGTATGATATAACGTGGAGGCAATGAGGAAGTTCCACCGAGGTCTGTCGTTAGCGGCTTTACAAAGCTGACCGGTGGACCCCACAGGATTACCCCTTCGCATGTTGAAGAGTCAAGCAGTCCCCGTCACGCCCTCTCCTGCGTAGGGCTCTGTG GGTATGATATAACGTGGAGGCAATGAGGAAGGCCCATTATATTGGCTTCCACCGAGGTCTGTCGTTAGCGGCTTTACAAAGCTGACCGGTGGACCCCACAGGATTACCCCTTCGCATGTTGAAGAGTCAAGCAGTCCCCGTCACGCCCTCTCCTGCGTAGGGCTCTGTG TGCTACGTCAGCTTCCCTAGATTTGTGACGTACAAAAAAGGTGTAAGCCAAACAGAAGTCATTATTGATCACTTAAGAATTCATGACTAAGATACCAACCCTTGCCTTATATATTCCTACGGCACCCAGCAGAGCGGAGTAGTCCCTCCGAGGCTGGCTCACAGTGATT CCGTGTCAGCTCTGCCCACTTATATATTGGTTATCTTCAGATGCCGATCACCCTATCCTCCTGGCTTAACTAAATGTATCTACATGCATATTATTGGCATCCTAAATTAAGCCTTGACTCTAACCGCTTGGTAAGGGGATCTATGATAGCGGGGTTTTGGTCACTAATC TCGAGCGCCTTATATATGACCGTCGCAATTTACTGACTATTAAGGACGCGCCTGTTATTCCTCCAAAGCTTCAGTATGGTGATGTCGCTCGTGTACCCCGGGAGCTAGTATCAACAGCAGCTTCATCGTTCCGTACTGAAAAATGTGCAATACAAAACCAATTTTAGAA GCCAGCCGCCACTTGCCACAGAAGGGGGTGTCGCCACTTATATTGGCAGAAGGGGGGAATGGCACCGGCTAAGACCGACCCCAATTTAACTCCTTACAAATCTCTGAGCCTCCACCCACCTCTCCCGACTTCAATCCAGATGCCGACTCCATAACTACTAACCACCAGA CTTCACCTAAGCGCAGCCGGTTTAGACAATGAATAGGAAAGACACCACTGTTACCCGATTCAGGCACTCGTCTGATAATTGCCGCCTTACTAATTGGCATAGGCTCACGGGCAAAGACAGTGCGTAACATTGTTCAACTGTCATACTAAACCAGTGGCGTGGCCTCTCG GTCGTCTACCGTGCACATAGCGAACCTGCTCGAATTGAGAGTATCTGTGGAGGTTATATATTGGCCGCCTGCCTGCGTTCCCGGCAAAACGCATTCTAGGACCATCGCTCCGGATGCGGTATCAGCACCATGGGGTACCTGGTCGCGTGGACGTTATCTGCTACCGGCT GGACTCTGCTCGGTTCGAAGCCCAGGATCAGTGTCCATATCATGGAAGCCTACGGTACCTACCAGTGGGGTATCTCTCGGTTCCGCTCCACGACGCGATTGCGCCAACGGCAGTTATCAGATTTCCTGGCCCTTATATATTGTAGTTGTATAGCTTTCACTCACACGGC AAGAAATACTCGATACTCAGTTTTAGATCGCCGCTGACTTTCAGCTTGCCTGCCTTAGTGATTGGCACGGGATTTGGGCTATTTTACAATATCTCATGGCAGTGTGAGTTAAGGCCTTCTGTAGAGCGGACGGGGTGAATCGCTTTCGACAAGGTTGGCTGTTTTCAAG CACGGTTAGCCTGGAATATTGGCTAATTGCAGGGAGGTACAGGCTAAACGTCGTGACTGTTCCCCTCTTGAGCGACGCTCTCGTCGATGGTAAGTGAATGCACCTTGCGTATACGCCTATTCGGGGCCTGTCACTTAATATACATCCTCGGGGGTGCACGTCAGTCGAT TGAAAGAGGACCTATTACTAGAGGTTACTGCACACCTACAGCGAGTGCCATAGTTAGAGGCACAAGGCAGACGGGCTATATGGTTCTCGTGACAAATGCCCCTGGTCGGCCGCCTTTCCTATTGGCCCAGAGAGCTGCCTGTACAGACCCGCCGTGGTTGGAGACTGAT CAAGACGGGACGCTGCTCCTTAGATTGAGAGTATTATAGAACCTCCGCAGGACAACAATTAATTCGCGTAGGCCTTGATTATTGGCTCGGTGGCAGTGGTCCGAGGAGTGATCTGTTGGTGTCTTAAAACTCTTTATTTCTCCTTTCGACGTTACTGAGACGGATTAGC CGACGGCACTCATCGTATTCGTGATGCACGCTGCCTGGGTTATGGGCTCTTCTTCTCCATACACGTCCAGGGAGACTGGCGGCCCGCCTTATATGGCGGCACTCGGTTCTCCGGTAGACATAGCCCGGCCGGGAAAGGAGGAGTTCATTAACGTTTGTTTAAACAGGAT TGACATTAAAGCCTTTGTCTGCATCGCATCAACAACGATGAGCGAGAGATCCTCTGAAGTTGCGGTGGGTACTGAGTTGCGTAGCGATTGGAGTGCGACATATATTGGCAGTAACATCATGATAACGATGGAATTAGGTGGCAGGCGATCGGCTACCGTCATAGAGTCT TGTAGTCGGGGCGCCTTATATACACGCGTATCGGCGGGTATCTCGATCATGTAATAGAATGGAATCAGTACGTGGTCACCACAATGGAAGGTGACCAGTAACGAGGTCTGACCCCGTAAAACGACGGTACGGCTCAGTCGAATGAGAGCCCCAAATTGTGAGCGATTTG GGGAATGTACTGACGGATGGGATGACCCTTATCGCTAGTTAATCCTCTCCATGCCTTATACCCTGGCCGTTTGGTTTTGAGAGGGGGACCGAAAAGACCTAGCAAAGATTAGTTTAGCTAATTCGCTTCCGGCTTAGATCGGTACCTCGAAGGACGGGCTCATCCGTTG TGGGTCTGGCGAGATGGTAGCATCCTCCGAGATCGACGTGCTTACTGCCTTATCCGTTGGCCGATTAGTGTTCATCAGTGGCAGCCACCCTGCAGTGCTTGGCTTACGCTACAGGTCACTCGTTAATACCCCCACTCCAATCTTAATCAACTAATTATAGCGAATCAAC GGAAATATATATTGGCTAAATCAACCTCTCTGGGGTCATAAATCGCCATATTCGGAGTTTTGGTTGTGCCGCATCCCTGCATATCACATGATGATTAGTCCTTTGGAAAGATGCACCGGGAGACTGCTCTAACGCAGGCCTGAGTTAGATGGTCCAAAAGCTGAGGCGA CTTGCCAGGACTCCGGGTAGATACCATGGGTCTGGGTTACGGGCTTGGTCACCTACGATCCGGTGTGCCCCCGTCTCAAAAGATGGGTGGCGTGCTCGATTGTCTGGTTTCCACACCGATCGCCTGGGATATTGGCCACCTCGACTGTTGGTAGGCGACCAGCAGGCAC'
Dna = string.split()

bestscore = float('inf')
bestmotif = []

for i in range(5000):
    ran = RandomizedMotifSearch(Dna, 15, 20)
    if (getScore(ran) < bestscore):
        bestscore = getScore(ran)
        bestmotif = ran

for b in bestmotif:
    print(b, end=' ')

