import sys

file = sys.argv[1]
output = sys.argv[2]

code = open(file,"r").read()

code = code.upper()
code = code.strip()
code = code.split()

labels={}

def generateDouble(text):
    output = ""
    for i in text:
        h = hex(ord(i))[2:5]
        if len(h) == 1:
            output += f"SV 0{h} PC "
        else:
            output += f"SV {h} PC "
    return output

for i in code:
    if i[len(i)-1] == ":":
        if len(hex(code.index(i))[2:5]) == 1:
            labels[i[:len(i)-1]] = f"0{hex(code.index(i))[2:5]}"
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

print(labels)

labeled_code = []

for i in code:
    if i in labels:
        labeled_code.append(labels[i])
    else:
        labeled_code.append(i)

out = open(output,"w")
out.write(" ".join(labeled_code))
