
def HammingDistance(one: str, two: str):

    mismatch = 0

    for i in range(0, len(one)):
        if not one[i:i+1] == two[i:i+1]:
            mismatch += 1

    return mismatch

def ApproximatePatternMatching(Pattern: str, Text: str, d: int):
    posi = []
    l = len(Pattern)

    for i in range(0, len(Text)-l+1):
        mis = HammingDistance(Text[i:i+l], Pattern)
        if mis <= d:
            posi.append(i)
    
    print(len(posi))

    return posi

file = open('dataset_865367_6.txt')

line1 = file.readline().strip()
line2 = file.readline().strip()
line3 = int(file.readline().strip())

hd = ApproximatePatternMatching(line1, line2, line3)

for h in hd:
    print(h, end=' ')

