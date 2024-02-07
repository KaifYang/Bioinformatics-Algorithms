
def ProfileMostProbableKmer(Text: str, k: int, Profile):
    
    maxpr = 0
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

file = open('dataset_865382_3.txt')

txt = file.readline().strip()
k = int(file.readline().strip())

Aline = file.readline().strip().split()
A = [float(a) for a in Aline]
Cline = file.readline().strip().split()
C = [float(c) for c in Cline]
Gline = file.readline().strip().split()
G = [float(g) for g in Gline]
Tline = file.readline().strip().split()
T = [float(t) for t in Tline]

profile = [A, C, G, T]

print(ProfileMostProbableKmer(txt, k, profile))