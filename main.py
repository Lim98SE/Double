import string
import sys
import os

tokens = {"PV":0,"PC":1,"SX":2,"SY":3,"IX":4,"IY":5,"DX":6,"DY":7,"SV":8,"IV":9,"DV":10,"RS":11,"CR":12,"GC":13,"GV":14,"XV":15,"YV":16,"JM":17,"CJ":18,"**":19}

charset = ""
charset+=(string.digits)
charset+=(string.ascii_uppercase)

special_chars = [" ",".",",","!","?","+","-","*","/","\"","\\","(",")","[","]","{","}","\n"]

code = ""

for i in special_chars:
    charset+=i

def tokenize_code(code):
    code = code.upper()
    code = code.strip()
    code = code.split()
    for i in code:
        if i[0] == "/":
            code.remove(i)
    for i in range(len(code)):
        if len(code[i])!= 2:
            print("All code should be two characters.")
            return [0]
        if code[i] in tokens:
            code[i] = tokens[code[i]]
    if len(code) > int("FF",base=16):
        print("Length cannot exceed 255.")
        return[0]
    return code

def run_code(code):
    data = [[0] * 256 for i in range(256)]
    
    X, Y, pointer = 0, 0, 0

    while pointer < len(code):
        opcode = code[pointer]
        if opcode == 0: # Print Value (PV)
            print(str(data[X][Y]) + "\n")
        elif opcode == 1: # Print Character (PC)
            print(charset[data[X][Y]%len(charset)],end="")
        elif opcode == 2: # Set X (SX)
            pointer+=1
            X = int(code[pointer], base=16)
        elif opcode == 3: # Set Y (SY)
            pointer+=1
            Y = int(code[pointer], base=16)
        elif opcode == 4: # Increment X (IX)
            X+=1
            X = X % 256
        elif opcode == 5: # Increment Y (IY)
            Y+=1
            Y = Y % 256
        elif opcode == 6: # Decrement X (DX)
            X-=1
            X = X % 256
        elif opcode == 7: # Decrement Y (DY)
            Y-=1
            Y = Y % 256
        elif opcode == 8: # Set Value (SV)
            pointer+=1
            data[X][Y] = int(code[pointer], base=16)
        elif opcode == 9: # Increment Value (IV)
            data[X][Y]+=1
            data[X][Y] = data[X][Y]%256
        elif opcode == 10: # Decrement Value (DV)
            data[X][Y]-=1
            data[X][Y] = data[X][Y]%256
        elif opcode == 11: # Restart (RS)
            pointer = -1
        elif opcode == 12: # Conditional Restart (CR)
            pointer += 1
            try:
                condition = int(code[pointer], base=16)
            except:
                condition = data[X][Y]
            if data[X][Y] != condition:
                pointer = -1
        elif opcode == 13: # Get Character (GC)
            try:
                data[X][Y] = charset.index(input("? ")[0].upper())
            except IndexError:
                data[X][Y] = 0
        elif opcode == 14: # Get Value (GV)
            try:
                data[X][Y] = int(input("? "),base=16)
            except:
                data[X][Y] = 0
            data[X][Y] = data[X][Y]%256
        elif opcode == 15: # Set Value to X (XV)
            data[X][Y] = X
        elif opcode == 16: # Set Value to Y (YV)
            data[X][Y] = Y
        elif opcode == 17: # Jump (JM)
            pointer+=1
            try:
                pointer=int(code[pointer], base=16)-1
            except:
                pointer=data[X][Y]-1
        elif opcode == 18: # Conditional Jump (CJ)
            pointer+=1
            try:
                condition = int(code[pointer], base=16)
            except:
                condition = data[X][Y]
            pointer+=1
            try:
                location = int(code[pointer], base=16)-1
            except:
                location = data[X][Y]-1
            if condition != data[X][Y]:
                pointer = location
        pointer+=1
    print("")

while True:
    # Shell Mode
    command = input("$ ").lower()
    command=command.split()
    if command[0] == "dir":
        print(os.getcwd())
        for x in os.listdir():
            print(x)
    if command[0] == "cd":
        try:
            os.chdir("".join(command[1:]))
        except Exception as e:
            print(e)
    if command[0] == "run":
        code = " ".join(command[1:])
        code = tokenize_code(code)
        run_code(code)
    if command[0] == "runfile":
        try:
            file = open(" ".join(command[1:]))
            code = file.read()
            file.close()
            code = tokenize_code(code)
            run_code(code)
        except Exception:
            print(e)

def charset_index_to_char(text):
    output=""
    text=text.upper()
    for i in text:
        output += f" {hex(charset.index(i))[2:5]} "
    return output
