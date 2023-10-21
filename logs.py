#!/usr/bin/env python3

import os
import logging

# BOILERPLATE -> Código repetitivo
# TODO: Usar função
# TODO: Usar lib(loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# instancia de log
log = logging.Logger("carlos", log_level) # <- Não é o root logger
# level
ch = logging.StreamHandler() # Seta a saida do handler
ch.setLevel(log_level) # Muda o level para debug
#formatacao
fmt = logging.Formatter( 
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)

"""
# root logger -> Logger principal do programa.
log.debug("Mensagem para o dev, QE, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execução")
log.critical("Erro geral, afeta todo mundo, ex: banco de dados sumiu")
"""

print("-----")
try:
    1/0
except ZeroDivisionError as e:
    log.error("[ERRO] Deu erro %s", str(e))
    # stdout -> print()
    # stderr <- interface para onde vão os erros

