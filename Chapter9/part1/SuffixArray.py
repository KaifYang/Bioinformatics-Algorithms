def SuffixArray(text):
    suffixes = []
    count = 0
    for i in range(len(text)):
        suffixes.append((text[i:], count))
        count += 1
    
    suffixes.sort()

    return suffixes

file = open('Chapter9\dataset_865525_2.txt')

string = file.readline().strip()

result = SuffixArray(string)

for r in result:
    print(r[1], end = ' ')