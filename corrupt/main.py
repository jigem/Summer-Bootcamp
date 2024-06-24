#Corrupt Office

#function for stack
def wala():
        print(line)
        print("Removed from line: ", line[-1])
        line.pop(-1)
        print(line)
#function for queue
def naa():
        print(line)
        print("Removed from line: ", line[0])
        line.pop(0)
        print(line)
#function for adding
def add():
    adding = int(input("Enter how many elements you want to add: "))
    for a in range (adding):
          element = int(input("Enter your element: "))
          line.append(element)
        

line = []
line_length = int(input("Enter the length of the line: "))

for l in range(1,line_length + 1):
        line.append(l)

print("Process Line: ", line)

for c in range(len(line)):
        w_add = (input("Do you want to add? yes or no: "))
        w_add.lower
        if w_add == "yes":
               add()
               print(line)
        elif w_add == "no":

            Boss_Status = input("Naa si boss wala? naa/wala: ")
            Boss_Status.lower

            #stack process if wala
            if Boss_Status == "wala":
                wala()

            #Que process if naa
            elif Boss_Status == "naa":
                naa()
                    
            else:
                    print("Invalid Input")
                    break
