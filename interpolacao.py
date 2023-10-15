
clientes = ["Bruno", "Carlos", "Henrique",]

email_tmpl ="""
Olá, %(nome)s
 
Tem interesse em comprar %(produto)s?
 
Este produto é ótimo para resolver
%(texto)s
 
Clique agora em %(link)s
 
Apenas %(quantidade)d disponiveis!
 
Preço promocional %(preco).2f
"""

for cliente in clientes:
    print(email_tmpl % {"nome": cliente, "produto": "caneta", "texto":"Escreve muito bem", 
          "link":"https://www.canetaslegais.com", "quantidade":1, "preco":50.5,})
