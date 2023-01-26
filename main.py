# Double v2.0
# New additions: Double Libraries! Use the package manager dbpk to get new libraries!

import string
import random
import sys

try:
    sys.argv[1]
except IndexError:
    print("Please provide arguments.")

if sys.argv[1] == "-r":
    code = " ".join(sys.argv[2:])
elif sys.argv[1] == "-f":
    try:
        with open(sys.argv[2]) as file:
            code = file.read()
    except:
        print("File not found/other error occured.")

tokens = {"PV": 0, "PC": 1, "SX": 2, "SY": 3, "IX": 4, "IY": 5, "DX": 6, "DY": 7, "SV": 8, "IV": 9, "DV": 10, "RS": 11,
          "CR": 12, "GC": 13, "GV": 14, "XV": 15, "YV": 16, "JM": 17, "CJ": 18, "**": 19, "JF": 20, "JB": 21, "CF": 22,
          "CB": 23, "GS": 24, "JR": 25, "RR": 26, "RC": 27, "BC": 28, "RN": 29, "US": 30, "DB": 31, "PS": 32, "+C": 33,
          "-C": 34, "IC": 35, "DC": 36, "SA": 37, "AV": 38, "PH": 39, "PL": 40}
libraries = {}


def generateDouble(text):
    output = "DB "
    for i in text:
        output += f"{ord(i)} "
    output += f"{0xFF}"
    return output


def tokenize_code(code):
    code = code.upper()
    lines = code.split("\n")

    final_lines = []

    for i in lines:
        if i[:len("IMPORT")] == "IMPORT":
            try:
                with open(f"libs/{i[len('IMPORT') + 1:]}.dblib") as lib:
                    exec(lib.read())
                    libraries[DATA["NAME"]] = [DATA, CODE, TOKENS]
                    global tokens
                    tokens.update(TOKENS)
                    print(f"Imported {DATA['NAME']} successfully")
                    INIT()

            except Exception as e:
                print(f"Error importing library: {e}")

            continue

        if "/" in i:
            final_lines.append(i[:i.find("/")])

        else:
            final_lines.append(i)

    code = "\n".join(final_lines)
    code = code.upper()
    code = code.strip()
    code = code.split()
    for i in range(len(code)):
        if code[i] in tokens:
            code[i] = tokens[code[i]]
    return code


def run_code(code):
    data = [[0] * 256 for i in range(256)]
    stack = []
    X, Y, pointer = 0, 0, 0
    acc = 0  # this too lmao

    while pointer < len(code):
        opcode = code[pointer]
        if opcode == 0:  # Print Value (PV)
            print(data[Y][X])
        elif opcode == 1:  # Print Character (PC)
            print(chr(data[Y][X]), end="")
        elif opcode == 2:  # Set X (SX)
            pointer += 1
            X = int(code[pointer])
        elif opcode == 3:  # Set Y (SY)
            pointer += 1
            Y = int(code[pointer])
        elif opcode == 4:  # Increment X (IX)
            X += 1
            X = X % 256
        elif opcode == 5:  # Increment Y (IY)
            Y += 1
            Y = Y % 256
        elif opcode == 6:  # Decrement X (DX)
            X -= 1
            X = X % 256
        elif opcode == 7:  # Decrement Y (DY)
            Y -= 1
            Y = Y % 256
        elif opcode == 8:  # Set Value (SV)
            pointer += 1
            data[Y][X] = int(code[pointer])
        elif opcode == 9:  # Increment Value (IV)
            data[Y][X] += 1
        elif opcode == 10:  # Decrement Value (DV)
            data[Y][X] -= 1
        elif opcode == 11:  # Restart (RS)
            pointer = -1
        elif opcode == 12:  # Conditional Restart (CR)
            pointer += 1
            try:
                condition = int(code[pointer])
            except:
                condition = data[Y][X]
            if data[Y][X] != condition:
                pointer = -1
        elif opcode == 13:  # Get Character (GC)
            try:
                data[Y][X] = ord(input("? ")[0])
            except IndexError:
                data[Y][X] = 255
        elif opcode == 14:  # Get Value (GV)
            try:
                data[Y][X] = int(input("? "))
            except:
                data[Y][X] = 255
            data[Y][X] = data[Y][X] % 256
        elif opcode == 15:  # Set Value to X (XV)
            data[Y][X] = X
        elif opcode == 16:  # Set Value to Y (YV)
            data[Y][X] = Y
        elif opcode == 17:  # Jump (JM)
            pointer += 1
            try:
                pointer = int(code[pointer]) - 1
            except:
                pointer = data[Y][X] - 1
        elif opcode == 18:  # Conditional Jump (CJ)
            pointer += 1
            try:
                condition = int(code[pointer])
            except:
                condition = data[Y][X]
            pointer += 1
            try:
                location = int(code[pointer]) - 1
            except:
                location = data[Y][X] - 1
            if condition != data[Y][X]:
                pointer = location
        elif opcode == 20:  # Jump Forward (JF)
            pointer += 1
            try:
                location = int(code[pointer])
            except:
                location = data[Y][X]
            pointer += location
        elif opcode == 21:  # Jump Backward (JB)
            pointer += 1
            try:
                location = int(code[pointer])
            except:
                location = data[Y][X]
            pointer -= location
        elif opcode == 22:  # Conditional Forward (CF)
            pointer += 1
            try:
                condition = int(code[pointer])
            except:
                condition = data[Y][X]
            pointer += 1
            try:
                location = int(code[pointer])
            except:
                location = data[Y][X]
            if data[Y][X] != condition:
                pointer += location
        elif opcode == 23:  # Conditional Forward (CB)
            pointer += 1
            try:
                condition = int(code[pointer])
            except:
                condition = data[Y][X]
            pointer += 1
            try:
                location = int(code[pointer])
            except:
                location = data[Y][X]
            if data[Y][X] != condition:
                pointer -= location
        elif opcode == 24:  # Get String (GS)
            string = input("? ")
            px = X
            datacodes = []
            for i in string:
                datacodes.append(ord(i))
            datacodes.append(255)
            for i in datacodes:
                X += 1
                data[Y][X] = i
            X = px
        elif opcode == 25:  # Jump to Subroutine (JR)
            pointer += 1
            try:
                location = int(code[pointer])
            except:
                location = data[Y][X]
            stack.append(pointer)
            pointer = location - 1
        elif opcode == 26:  # Return from Subrotine (RR)
            pointer = stack.pop()
        elif opcode == 27:  # Conditional Jump to Subroutine (RC)
            pointer += 1
            try:
                condition = int(code[pointer])
            except:
                condition = data[Y][X]
            pointer += 1
            try:
                location = int(code[pointer])
            except:
                location = data[Y][X]
            if data[Y][X] != condition:
                stack.append(pointer)
                pointer = location - 1
        elif opcode == 28:  # Conditional Return from Subroutine (CB)
            pointer += 1
            try:
                condition = int(code[pointer])
            except:
                condition = data[Y][X]
            if data[Y][X] != condition:
                pointer = stack.pop()
        elif opcode == 29:  # Random Byte (RN)
            data[Y][X] = random.randint(0, 255)
        elif opcode == 31:  # Data Block (DB)
            mp = (Y, X)
            pointer += 1
            while int(code[pointer]) != 0xFF:
                X += 1
                X = X % 0xFF
                data[Y][X] = int(code[pointer])
                pointer += 1
            Y, X = mp
        elif opcode == 32:  # Print String (PS)
            mp = (Y, X)
            X += 1
            while data[Y][X] != 0xFF:
                print(chr(data[Y][X]), end="")
                X += 1
            Y, X = mp
        elif opcode == 33:  # Add Cell to ACC (+C)
            acc += data[Y][X]
        elif opcode == 34:  # Subtract Cell from ACC (-C)
            acc -= data[Y][X]
        elif opcode == 35:  # Increment ACC (IC)
            acc += 1
        elif opcode == 36:  # Decrement ACC (DC)
            acc -= 1
        elif opcode == 37:  # Set ACC (SA)
            pointer += 1
            acc = int(code[pointer])
        elif opcode == 38:  # Get ACC Value (AV)
            data[Y][X] = acc
        elif opcode == 39:  # Push Value (PH)
            stack.append(data[Y][X])
        elif opcode == 40:  # Pull Value (PL)
            data[Y][X] = stack.pop()

        for lib in libraries:
            exec(libraries[lib][1])

        pointer += 1


code = tokenize_code(code)
run_code(code)
