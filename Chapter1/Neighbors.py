
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

file = open('dataset_865370_4.txt')

line1 = file.readline().strip()
line2 = int(file.readline().strip())

ne = Neighbors(line1, line2)

for n in ne:
    print(n, end=' ')