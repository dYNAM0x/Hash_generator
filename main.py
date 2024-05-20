import sys,signal
from banner import *
from text_hash import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == "__main__":
        
    tittle()
    if len(sys.argv) == 1:
        print(f"{bcolors.FAIL}[!]{bcolors.ENDC}Uso: python3 main.py <texto>")
    else:
        text_to_hash(sys.argv[1])
