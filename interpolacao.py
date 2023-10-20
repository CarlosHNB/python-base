"""
Olá, %(nome)s
 
Tem interesse em comprar %(produto)s?
 
Este produto é ótimo para resolver
%(texto)s
 
Clique agora em %(link)s
 
Apenas %(quantidade)d disponiveis!
 
Preço promocional %(preco).2f

Uso: 
    python3 interpolacao.py emails.txt email_tmpl
    
"""
__version__ = "0.1.1"
__author__ = "CarlosHNB"


import os
import sys


arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de emails")
    sys.exit()
    
filename = arguments[0]
templatename = arguments[1]

print(filename, templatename)

path = os.curdir
filepath = os.path.join(path , filename)
templatepath = os.path.join(path, templatename)


for line in open(filepath):
    name, email = line.split(",")
    
    # TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    
    print(open(templatepath).read() % {
        "nome": name.capitalize(), 
        "produto": "caneta", 
        "texto":"Escreve muito bem", 
          "link":"https://www.canetaslegais.com", 
          "quantidade":1, 
          "preco":50.5,
          }
        )
    
    print("-" * 45)