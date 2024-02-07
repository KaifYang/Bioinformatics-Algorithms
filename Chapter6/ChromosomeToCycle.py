def ChromosomeToCycle(Chromosome):
    Nodes = [None] * (len(Chromosome)*2)
    
    #j is the index on the chromosome
    for j in range(1, len(Chromosome)+1):
        i = Chromosome[j-1]

        if i > 0:
            Nodes[(2*j-1) - 1] = 2*i - 1
            Nodes[(2*j) - 1] = 2*i
        
        #since i < 0 we need to reverse its sign to make the indexing work
        else:
            Nodes[(2*j-1) - 1] = -(2*i)
            Nodes[(2*j) - 1] = -(2*i) - 1
    
    return Nodes 

Chromosome = '+1 -2 -3 +4'
Chromosome = Chromosome.split()
Chromosome = [int(i) for i in Chromosome]

Nodes = ChromosomeToCycle(Chromosome)

print('(', end = '')

for n in Nodes:
    if not n == Nodes[len(Nodes)-1]: 
        print(n, end = ' ')
    else:
        print(n, end = '')
print(')', end = '')
