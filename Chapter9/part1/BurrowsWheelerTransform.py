def BurrowsWheelerTransform(text):
    #get all cyclic rotation of the text
    rotations = []

    for i in range(len(text)):
        rotations.append(text[-i:] + text[:-i])
    
    #print(rotations)

    rotations.sort()

    BWT = ''

    for r in rotations:
        BWT += r[-1]

    return BWT

file = open('Chapter9\dataset_865526_5.txt')
string = file.readline().strip()

print(BurrowsWheelerTransform(string))