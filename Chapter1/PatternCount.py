def PatternCount(Text: str, Pattern: str) -> int:
    count = 0
    
    for i in range(0, len(Text) - len(Pattern) + 1):
        
        if (Text[i:(i + len(Pattern))] == Pattern):
            print(1)
            count = count + 1
    
    return count


file = open('dataset_865361_6.txt')

lines = file.readlines()

print(lines[0])

print(lines[1])

print(PatternCount(lines[0], lines[1]))




