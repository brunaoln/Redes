#!/usr/bin/python
# -*- coding: utf-8 -*
import route
import socket
import threading
import time
from collections import deque

#definir max size para os campos
TAMANHO_TABELA = 500 
tabela = deque(maxlen = TAMANHO_TABELA) # create a deque with SIZE_BUFFER positions
PORT = 9999
timeout = 1 # DECLAREI UM VALOR ALEATORIO PARA TIMEOUT

def le_arquivo(file, tabela):
	global TAMANHO_TABELA
	with open(file, "rb") as f:
		while True: 
			c = f.read(1350) #1350
			#se acabou o arquivo
			if not c:
				print "End of file\n"
				exitFlag = 1
				break
			#enquanto o buffer estiver cheio
			while (len(tabela) >= TAMANHO_TABELA):
				#print("Full Buffer\n")
				continue
			while True:
				try:
					tabela.appendleft(c)
					break
				except:
					continue
	return

class ThreadEnviaTabela (threading.Thread):
    def __init__():
        threading.Thread.__init__(self)

    def run(self):
	global tabela
 	
 	route.


def main():
    #PORT = parametro de entrada
	global tabela
    
    teste = myThread(0, 0, "entrada.pdf", 0, Tam_arq) #esta funcionando
    teste.start()

    teste2 = myThread(1, 0, "entrada.pdf", 1, Tam_arq)
    teste2.start()

if __name__ == "__main__":
        main()
