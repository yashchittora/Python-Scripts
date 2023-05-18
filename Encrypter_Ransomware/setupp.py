import importlib

def check(x):
    try:
        importlib.import_module(x)
        # print(f"{x} is already installed.")
    except ImportError:
        print(f"{x} is not installed. \n->Installing Dependencies...")
        
        install_module(x)

def install_module(x):
    from subprocess import check_call,CalledProcessError
    try:
        check_call(["pip", "install", x])
        print(f"{x} has been successfully installed.")
    except CalledProcessError:
        print(f"Failed to install {x}. Please make sure you have pip installed.")

def inp(l):
    for i in l:
        check(i)