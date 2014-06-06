#!/usr/bin/python
# -*- coding: utf-8 -*

import route
import socket
import threading
import time
import sys
from netifaces import interfaces, ifaddresses, AF_INET
#from collections import dequee
#tabela = route.router()
tabela = None
#tabela = deque(maxlen = TAMANHO_TABELA) # create a deque with SIZE_BUFFER positions
PORT = 9999 #porta com a qual sera feita a conexao
timeout = 1 # DECLAREI UM VALOR ALEATORIO PARA TIMEOUT
TEMPO_PARA_REENVIO = 60 #periodo (em segundos) para enviar mensagem de rotina


class ThreadEnviaTabela (threading.Thread):
	global tabela
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		tabela.enviaTabela()
 	#envia periodicamente seu vetor de distancias

class ThreadRecebeTabela (threading.Thread):
	global tabela
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		tabela.recebeTabela()
 	#recebeTabela vai receber a tabela de um de seus vizinhos, em seguida enviará um ACK, e por fim mandará
 	# seu vetor de distâncias atualizado para outros,
class InterfacesInfo:
	ifinfo = None
	addr = None
	netmask = None
	def __init__(self, ifinfo, addr, netmask):
		self.ifinfo = ifinfo
		self.addr = addr
		self.netmask = netmask
	

def main():
    #PORT = parametro de entrada
	global tabela
	
	lista_Interfaces = list()
	argumentos = sys.argv[1:]
	host_name = ""
    	for i in xrange(len(argumentos)):
    		if argumentos[i] == '-h':
    			host_name = argumentos[i+1]
    	tabela = route.router(host_name)
    	
    	for ifName in interfaces():
    		ifinfo = ifaddresses(ifName).setdefault(AF_INET)[0]
    		addr = ifinfo['addr']
    		netmask = ifinfo['netmask']
    		aux = InterfacesInfo(ifinfo, addr, netmask)
    		lista_Interfaces.append(aux)
    	
	enviar = ThreadEnviaTabela()
	enviar.start()

	receber = ThreadRecebeTabela()
	receber.start()

if __name__ == "__main__":
	main()
