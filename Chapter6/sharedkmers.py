
#get reverse complement of a dna sequence
def RV(text):
    comp = ''

    for i in range(0, len(text)+1):
        if text[i:i+1] == 'A':
            comp = 'T' + comp
        elif text[i:i+1] == 'T':
            comp = 'A' + comp
        elif text[i:i+1] == 'C':
            comp = 'G' + comp
        elif text[i:i+1] == 'G':
            comp = 'C' + comp

    return comp


def sharedkmers(k, str1, str2):
    posi = []

    for i in range(len(str1)-k+1):
        kmer1 = str1[i:i+k]

        for j in range(len(str2)-k+1):
            kmer2 = str2[j:j+k]



            if kmer1 == kmer2 or RV(kmer1) == kmer2:
                posi.append((i, j))
    
    return posi

file = open('Chapter6\dataset_865471_5.txt')

k = int(file.readline().strip())
str1 = file.readline().strip()
str2 = file.readline().strip()

result = sharedkmers(k, str1, str2)

for r in result:
    print('(' + str(r[0]) + ', ' + str(r[1]) + ')')