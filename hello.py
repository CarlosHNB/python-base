#!/usr/bin/env python3
"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe atraves do CLI argument `--lang`
    ex: ./hello.py --lang="LANG"
Ou o usuário terá que digitar
Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__= "Carlos Henrique"
__license__= "Unlicense"

import os
import sys

# os.environ (dict like object <- se comporta como um dict)
# os.environ["KEY"]

arguments = {"lang": None,"count": 1,}

for arg in sys.argv[1:]: # Todos os itens que começam do item 1 até o último.
    
    try:
        key, value = arg.split("=") # Recebe os argumentos e desempacota.
    
    except ValueError as e:
        # TODO: Loggin
        print(f"[ERROR] {str(e)}")
        print("You need to use `=`")
        print(f"You passed {arg}")
        print("try with --key=value")
        sys.exit()
        
    #lstrip("-") -> Remove todos os caracteres do parenteses, no lado esquerdo.
    key = key.lstrip("-").strip() # .strip() remove os espaços, evitando erros.
    value = value.strip()

    # Validação
    if key not in arguments:
        print(f"Invalid Option `{key}`")    
        sys.exit()
    
    arguments[key] = value
    
current_language = arguments["lang"]

if current_language is None:
   if "LANG" in os.environ:
       # TODO: Usar repetição
        current_language = os.getenv("LANG")
    
   else:
        current_language = input("Choose a language:")
    
current_language = current_language[:5]


msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

"""
try com valor default
message = msg.get(current_language)

"""

try:
    message = msg[current_language]
except KeyError as e:
    
    print(f"Language {str(e)} is invalid, choose from {list(msg.keys())}")
    sys.exit()

  
print(message * int(arguments["count"]))