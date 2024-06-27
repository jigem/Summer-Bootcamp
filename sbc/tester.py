fag = {}

with open("text.txt") as file:
        for line in file:
            (x, y) = line.split(':')
            fag[x] = y
print(fag)