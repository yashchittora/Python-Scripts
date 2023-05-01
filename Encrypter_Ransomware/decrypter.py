import os
from cryptography.fernet import Fernet
import datetime

files = []

for file in os.listdir():
    if file == 'encrypter.py' or file == 'thekey.key' or file == 'decrypter.py' or file == 'encrypt_log.txt' or file == 'decrypt_log.txt':
        continue
    
    if os.path.isfile(file):
        files.append(file)

print(f"\nFiles to be Decrypted : {files}")

main_pass = "admin@qwerty"
usr_pass = input("\nEnter Secret Password \n->")
if usr_pass == main_pass:

    print("Right Password Buddy")
    with open("thekey.key","rb") as keyfile:
        key = keyfile.read()

    for file in files:
        with open(file,'rb') as targetFile:
            enc_contents = targetFile.read()
            dec_contents = Fernet(key).decrypt(enc_contents)
        
        with open(file,'wb') as targetFile:
            targetFile.write(dec_contents)

    print(f"\n{len(files)} file Decrypted Successfully")

    with open("decrypt_log.txt","a") as log:
        
        timestamp = datetime.datetime.now()
        data_log = f"Files encrypted on {timestamp} \nNumber of Files Decrypted : {len(files)} \nFiles Decrypted : {files} \nKey : {key} \n\n"
        
        log.write(data_log)

else:
    print("Haha , No Chance Buddy , You entered wrong password")



