x = 0
y = [0]*30000
z = 0
brainfuck = input()
brainfuck.split
print (brainfuck)
for i in brainfuck:
    x+= 1
    if brainfuck[x] == (">"):
        z += 1
    elif brainfuck[x] == ("<"):
        z -= 1
    elif brainfuck[x] == ("+"):
        y[z] += 1
    elif brainfuck[x] == ("-"):
        y[z] -= 1
    elif brainfuck[x] == ("["):
        if y[z] == 0:
            #function to skip to closing bracket
    elif brainfuck[x] == ("]"):
        if y[z] != 0:
            #function to skip to opening bracket
    elif brainfuck[x] == (","):
        cell = input("Input a value: ")
        cell = ord(cell)
        y[z] = cell
    elif brainfuck[x] == ("."):
        output = #function to convert ASCII to value
        print (output)
    else:
        continue
