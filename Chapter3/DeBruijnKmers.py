from collections import defaultdict

def DeBruijnKmers(kmers: list[str]):
    graph = defaultdict(list)

    for k in kmers:
        prefix = k[:-1]
        suffix = k[1:]

        graph[prefix].append(suffix)
    
    return graph

file = open('dataset_865400_8.txt')

txt = file.readline().split()

graph = DeBruijnKmers(txt)

output = open('output', 'w')

for key in graph:

    string = key + ': '
    for g in graph[key]:
        string = string + g + ' '
    
    string = string[:-1]

    output.write(string + "\n")