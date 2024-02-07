from collections import defaultdict

def CycleToChromosome(Nodes):
    Chromosome = [0] * (len(Nodes)//2)

    for j in range(1, len(Nodes)//2 + 1):
        if Nodes[(2*j-1) - 1] < Nodes[(2*j) - 1]:
            Chromosome[j - 1] = int(Nodes[(2*j) - 1]/2)

        else:
            Chromosome[j - 1] = -int(Nodes[(2*j-1) - 1]/2)

    return Chromosome

Nodes = '2 1 3 4 5 6 7 8 10 9 12 11 13 14 16 15 17 18 19 20 22 21 23 24 25 26 28 27 29 30 31 32 34 33 36 35 37 38 39 40 42 41 44 43 46 45 48 47 50 49 52 51 54 53 56 55 58 57 59 60 62 61 64 63 65 66 68 67 70 69 71 72 74 73 75 76 77 78 79 80 82 81 84 83 85 86 88 87 89 90 91 92 94 93 95 96 97 98 99 100 102 101 103 104 105 106 107 108 109 110 111 112 114 113 116 115 118 117 120 119 121 122 123 124 126 125'
Nodes = Nodes.split()
Nodes = [int(i) for i in Nodes]

Chromosome = CycleToChromosome(Nodes)

print('(', end = '')

for c in Chromosome:
    if not c == Chromosome[len(Chromosome)-1]: 
        if c > 0:
            print('+' + str(c), end = ' ')
        else:
            print(c, end = ' ')
    else:
        if c > 0:
            print('+' + str(c), end = '')
        else:
            print(c, end = '')

print(')', end = '')