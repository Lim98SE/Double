import sys

file = sys.argv[1]
output = sys.argv[2]

code = open(file,"r").read()

code = code.upper()
code = code.strip()
code = code.split()

labels={}

for i in code:
    if i[len(i)-1] == ":":
        if len(hex(code.index(i))[2:5]) == 1:
            labels[i[:len(i)-1]] = f"0{hex(code.index(i))[2:5]}"
        else:
            labels[i[:len(i)-1]] = hex(code.index(i))[2:5]
        code.pop(code.index(i))

print(labels)

labeled_code = []

for i in code:
    if i in labels:
        labeled_code.append(labels[i])
    else:
        labeled_code.append(i)

out = open(output,"w")
out.write(" ".join(labeled_code))
