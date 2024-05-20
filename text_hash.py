from main import bcolors

def text_to_hash(texto):
    hash_text = hash(texto) 
    print(f"{bcolors.OKGREEN}[+]{bcolors.ENDC}Texto convertido a hash: {bcolors.OKBLUE}{hash_text}{bcolors.ENDC}")