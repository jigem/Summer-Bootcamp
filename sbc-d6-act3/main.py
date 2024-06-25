string = "*"
rows = 6
for i in range(rows, 1, -1):
    print(string * i)
for l in range (1):
    spaces = " " * (rows - i) 
    stars = string * 1  
    line = stars + spaces + stars
    print(line)
for i in range(2,rows + 1):
    print(string * i)

