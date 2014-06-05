#!/usr/bin/python
# -*- coding: utf-8 -*

import socket
import threading
import time
from collections import deque
import select


#definir max size para os campos
SIZE_BUFFER = 500 
exitFlag = 0
countBuff = 0
buff = deque(maxlen = SIZE_BUFFER)
PORT = 9999
Tam_arq = -1
timeout = 1 # DECLAREI UM VALOR ALEATORIO PARA TIMEOUT

def le_arquivo(file, buff):
	global SIZE_BUFFER, exitFlag
	with open(file, "rb") as f:
		while True: 
			c = f.read(1350) #1350
			#se acabou o arquivo
			if not c:
				print "End of file\n"
				exitFlag = 1
				break
			#enquanto o buffer estiver cheio
			while (len(buff) >= SIZE_BUFFER):
				#print("Full Buffer\n")
				continue
			while True:
				try:
					buff.appendleft(c)
					break
				except:
					continue
	return

