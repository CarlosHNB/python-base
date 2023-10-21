#!/usr/bin/env python3
"""Calculadora prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mult -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefix.py
operação: sum
n1: 5
n2: 
4
9

Os resultados serão salvos em `prefixcalc.log`
"""
__version__ = "0.1.0"
__author__ = "CarlosHNB"

import os
import sys
from datetime import datetime

arguments = sys.argv[1:]

# Validação
if not arguments:
    operation = input("Operação:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
    
elif len(arguments) != 3: 
    print("Número de argumentos inválidos")
    print("ex: `sum 5 2`")
    sys.exit(1)

operation, *nums = arguments


valid_operations = ("sum", "sub", "mult", "div")

if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: Repetição while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit()
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)
  

n1, n2 = validated_nums


# TODO: Usar dict de funções
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mult":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

# Gravando o log no arquivo `prefixcalc.log`
path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

print(f"O resultado é {result}")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")

except PermissionError as e:
    print(str(e))
    sys.exit()
    
    
