
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


def MaxMap(map):
    max = float('-inf')

    for key in map:
        if map[key] > max:
            max = map[key]
    
    return max


def FrequentWords(Text: str, k: int):
    fp = []
    map = FrequencyTable(Text, k)
    max = MaxMap(map)

    for key in map:
        if map[key] == max:
            fp.append(key)
    
    return fp


text = 'CAAGGTGCTCCGGAGGCTATTCGTCTATTCGTCAATTGTCAATTGTCCAAGGTGCCTGTTCCCGCTGTTCCCGCAAGGTGCCTGTTCCCGAATTGTCTATTCGTCCTGTTCCCGTCCGGAGGCTCCGGAGGCAATTGTCTATTCGTCTCCGGAGGCCTGTTCCCGTATTCGTCAATTGTCCTGTTCCCGCTGTTCCCGTATTCGTCCAAGGTGCTCCGGAGGCTATTCGTCAATTGTCCTGTTCCCGTCCGGAGGCTCCGGAGGCCTGTTCCCGTCCGGAGGCTATTCGTCCTGTTCCCGTCCGGAGGCTATTCGTCAATTGTCTATTCGTCCTGTTCCCGCTGTTCCCGCTGTTCCCGAATTGTCTATTCGTCAATTGTCAATTGTCCTGTTCCCGAATTGTCTATTCGTCCTGTTCCCGCAAGGTGCTATTCGTCTCCGGAGGCTCCGGAGGCCTGTTCCCGCAAGGTGCAATTGTCTATTCGTCCAAGGTGCTCCGGAGGCTCCGGAGGCCTGTTCCCGAATTGTCCAAGGTGCAATTGTCTCCGGAGGCCAAGGTGCCTGTTCCCGCAAGGTGCCAAGGTGCTATTCGTCCTGTTCCCGCTGTTCCCGTATTCGTCTATTCGTCTATTCGTCCTGTTCCCGCTGTTCCCGTCCGGAGGCTATTCGTCCAAGGTGCCAAGGTGCTCCGGAGGCTATTCGTCTCCGGAGGCTATTCGTCAATTGTCTCCGGAGGCCTGTTCCCGTATTCGTCCAAGGTGCAATTGTCCTGTTCCCGTCCGGAGGCAATTGTCCAAGGTGCCAAGGTGCCTGTTCCCGCTGTTCCCGTCCGGAGGCCTGTTCCCGCTGTTCCCGCAAGGTGCCTGTTCCCGCAAGGTGCCAAGGTGC'

print(FrequentWords(text, 11))