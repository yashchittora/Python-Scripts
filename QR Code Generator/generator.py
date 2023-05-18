import setupp
modules_used = ["qrcode"]
setupp.inp(modules_used)

from qrcode import *
from subprocess import run

def inp():
    global link
    try:
        link = input("Enter link : ")
    except:
        inp()

try:
    inp()
except:
    print(Exception)
    inp()

try:
    qr = make(link)
    print("QR Code generated successfully")
    qr.save("code.jpg")
    run(["open","code.jpg"])
    
except:
    print(Exception)
    