def FrequencyTable(Text, k):
    table = {}
    n = len(Text)

    for i in range(0, n-k+1):
        Pattern = Text[i:i+k]
        if Pattern not in table:
            table[Pattern] = 1
        else:
            table[Pattern] += 1
    
    return table


def ClumpFinding(Text, k, L, t):
    Patterns = []
    n = len(Text)

    for i in range(0, n-L+1):
        Window = Text[i:i+L]
        freqMap = FrequencyTable(Window, k)
        for key in freqMap:
            if freqMap[key] >= t:
                Patterns.append(key)
    
    #remove duplicates
    Patterns = list(set(Patterns))

    return Patterns


txt = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'

k = 5
l = 50
t = 4

patt = ClumpFinding(txt, k, l, t)

print(len(patt))

for i in patt:
    print(i, end=' ')