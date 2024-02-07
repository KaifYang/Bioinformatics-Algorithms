
def MinimumSkew(Genome: str):
    posi = []
    
    skew1 = 0
    minimum = 0

    for i in range(0, len(Genome)):
        if Genome[i:i+1] == 'C':
            skew1 = skew1-1
        elif Genome[i:i+1] == 'G':
            skew1 = skew1+1
        
        if skew1 < minimum:
            minimum = skew1
    
    skew2 = 0

    for j in range(0, len(Genome)):
        if Genome[j:j+1] == 'C':
            skew2 = skew2-1
        elif Genome[j:j+1] == 'G':
            skew2 = skew2+1

        if skew2 == minimum:
            posi.append(j+1)
    
    if minimum == 0:
        posi.append(0)

    return posi

file = open('dataset_865366_10.txt')

txt = file.read()

ms = MinimumSkew(txt)

for i in ms:
    print(i, end=' ')