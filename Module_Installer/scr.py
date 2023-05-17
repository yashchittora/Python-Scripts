import importlib

def check(x):
    try:
        importlib.import_module(x)
        print(f"{x} is already installed.")
    except ImportError:
        a = input((f"{x} is not installed. \nDo you want to install ? [Y/N] \n->"))
        
        if a in ['Y','y']:
            install_module(x)

def install_module(x):
    from subprocess import check_call,CalledProcessError
    try:
        check_call(["pip", "install", x])
        print(f"{x} has been successfully installed.")
    except CalledProcessError:
        print(f"Failed to install {x}. Please make sure you have pip installed.")


m = input("Enter Module Name : ")
check(m)




