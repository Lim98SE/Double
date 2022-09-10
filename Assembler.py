# assembler update?????

import sys

file = sys.argv[1]
output = sys.argv[2]

code = open(file,"r").read()

code = code.upper()
code = code.strip()
code = code.split()

labels = {}
variables = {}

def generateDouble(text):
    output = "DB "
    for i in text:
        output += f"{ord(i)} "
    output += f"{0xFF}"
    return output

for i in code:
    if i[len(i)-1] == ":":
        if len(hex(code.index(i))[2:5]) == 1:
            labels[i[:len(i)-1]] = f"code.index(i)"
        else:
            labels[i[:len(i)-1]] = hex(code.index(i))[2:5]
        code.pop(code.index(i))
    if i[0] == "/":
        code.pop(code.index(i))
    if i[0] == ".":
        code[code.index(i)] = generateDouble(i[2:len(i)-1].replace("~", " "))
    if "#" in i:
        char = i[i.find("#")+1]
        index = code.index(i)
        h = hex(ord(char))[2:5]
        if len(h) == 1:
            i = i.replace(f"#{char}","0"+h)
        else:
            i = i.replace(f"#{char}",h)
        code[index] = i
    if i[0] == "$":
        if "=" in i:
            c = i.split("=")
            variables[c[0]] = c[1]

print(labels, variables)

labeled_code = []

for i in code:
    if i in labels:
        labeled_code.append(labels[i])
    elif i in variables:
        labeled_code.append(variables[i])
    else:
        labeled_code.append(i)

out = open(output,"w")
out.write(" ".join(labeled_code))

print("Make sure to remove variable definitions!")
