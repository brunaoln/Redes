#!/usr/bin/python
# -*- coding: utf-8 -*

import route
import socket
import threading
import time
#from collections import deque
tabela = route.router()
#tabela = deque(maxlen = TAMANHO_TABELA) # create a deque with SIZE_BUFFER positions
PORT = 9999 #porta com a qual sera feita a conexao
timeout = 1 # DECLAREI UM VALOR ALEATORIO PARA TIMEOUT
TEMPO_PARA_REENVIO = 60 #periodo (em segundos) para enviar mensagem de rotina



class ThreadEnviaTabela (threading.Thread):
	global tabela
    def __init__():
        threading.Thread.__init__(self)

    def run(self):
 		tabela.enviaRotina()
 	#envia periodicamente seu vetor de distancias

class ThreadRecebeTabela (threading.Thread):
	global tabela
    def __init__():
        threading.Thread.__init__(self)

    def run(self):
 		tabela.recebeTabela()
 	#recebeTabela vai receber a tabela de um de seus vizinhos, em seguida enviará um ACK, e por fim mandará
 	# seu vetor de distâncias atualizado para outros,


def main():
    #PORT = parametro de entrada
	global tabela
    
    enviar = ThreadEnviaTabela()
    enviar.start()

    receber = ThreadRecebeTabela()
    receber.start()

if __name__ == "__main__":
        main()
