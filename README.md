# Double
An esolang where every character has a partner.

## Commands
PV - **P**rint **V**alue - Prints the value of the current cell.
PC - **P**rint **C**haracter - Prints the character set index of the current cell.
SX - **S**et **X** - Sets the X coordinate of the selected cell.
SY - **S**et **Y** - Sets the Y coordinate of the selected cell.
IX - **I**ncrement **X** - Increments the X coordinate.
IY - **I**ncrement **Y** - Increments the Y coordinate.
DX - **D**ecrement **X** - Decrements the X coordinate.
DY - **D**ecrement **Y** - Decrements the Y coordinate.
SV - **S**et **V**alue - Sets the value of the current cell.
IV - **I**ncrement **V**alue - Increments the value of the selected cell.
DV - **D**ecrement **V**alue - Decrements the value of the selected cell.
RS - **R**e**S**tart - Restarts the program.
CR - **C**onditional **R**estart - Restarts the program if the value after the instruction is **not** equal to the cell's value.
GC - **G**et **C**haracter - Gets the charset ID of the character the user inputs. Returns 0 if invalid.
GV - **G**et **V**alue - Gets the value of the number the user inputs.
XV - **X** **V**alue - Sets the cell's value to the X coordinate.
YV - **Y** **V**alue - Sets the cell's value to the Y coordinate.

## Using the Program
It first starts up in Shell Mode, where you can run code by typing **run** and the code,
open a file containing code by typing **runfile** and the filename,
change your directory by typing **cd** and the directory to change to,
and view all files in the directory by typing **dir**.

## Example Programs
### Hello, World!
```
SV 11 PC
SV 0E PC
SV 15 PC PC
SV 18 PC
SV 26 PC
SV 24 PC
SV 20 PC
SV 18 PC
SV 1B PC
SV 15 PC
SV 0D PC
SV 27 PC
```

### [Hello](https://esolangs.org/wiki/Hello) Interpreter
```
GC CR 11
SV 11 PC
SV 0E PC
SV 15 PC PC
SV 18 PC
SV 26 PC
SV 24 PC
SV 20 PC
SV 18 PC
SV 1B PC
SV 15 PC
SV 0D PC
SV 27 PC
```

### Adder (created by vivax3794)
```
DV IX IV DX CR FF IX DV PV GV DX GV RS
```

## File Format
Plain-text files storing code can be opened as **.txt** or **.dbl** files.

## Licence
Do whatever you want, as long as you credit me.
