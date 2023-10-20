#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
    Texto Exemplo

$notes.py read --tag=tech
....
....
....
"""

__version__ = "0.0.1"
__author__ = "CarlosHNB"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")
arguments = sys.argv[1:]

if not arguments:
    print("Invalid usage")
    sys.exit()


cmds = ("read", "new")

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    # Leitura das notas
    
    with open(filepath, "r") as note:
        pass
            
if arguments[0] == "new":
    # Criação das notas
    with open(filepath, "a") as note:
       pass