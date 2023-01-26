import requests
import sys
import os

args = sys.argv
type = args[1].lower()
text = " ".join(args[2:])

url = f"https://dbpk.pythonanywhere.com/{type}?query={text}"

response = requests.get(url)

try:
    os.chdir("libs")

except Exception:
    os.mkdir("libs")
    os.chdir("libs")

if response.text.split("\n")[-1] == "# Found package!":
    with open(f"{text.upper()}.dblib", "w") as lib_file:
        lib_file.write(response.text)
        print(f"Installed {text.upper()}.dblib")

elif "not found" in response.text:
    print("Package not found!")

elif "[" in response.text:
    found = eval(response.text)

    print("Found packages:")

    for i in found:
        print(i)

else:
    print(f"Something happened... {response.text}")