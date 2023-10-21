#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to Ask Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)


try:
    names = open("names.txt").readlines() # FileNotFoundError
except FileNotFoundError as e: # Bare excep -> Captura qualquer exception.
    print(f"{str(e)}")
    sys.exit(1)
    # TODO: Usar retry

else: # Ocorre somente quando não ocorre a exception
    print("Sucesso!!")

finally: # Sempre será executado
    print("Execute isso sempre")
    
        
try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)


