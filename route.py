import time
from collections import deque
from socket import *
import subprocess

MAX_ROUTES = 64
MAX_TTL = 120 #tempo
INFINITO = 65 #maior que a maxima distancia que um host pode estar do outro
MUDANCA = 0
TEMPO_ROTINA = 300 #tempo para enviar o quadro de rotina

# Nossas mensagens terao como primeiro campo que contem um numero de classificacao da mensagem:
#        0 -> ACK para mensagem de rotina
#        1 -> ACK para mensagem de mudanca
#        2 -> a mensagem eh de rotina
#        3 -> a mensagem eh de mudanca

TAMANHO_MENSAGEM = 1000
MAXIMO_NUMERO_TENTATIVAS = 6

def route:
    dest = 0
    nexthop = 0
    cost = 0
    ttl = 0
    def __init__(dest, nexthop, cost, ttl=120):
        self.dest = dest
        self.nexthop = nexthop
        self.cost = cost
        self.ttl = ttl

def unpack(dados, nexthop):
    #guarda o numero de rotas daquela tabela
    num_routes = int(dados[0:2])
    newRoutes = []
    j = 2
    for (i in range (0, num_routes)):
        #cria rotas com os dados do pacote
        newRoutes.append(route(j:(j + 13)], nexthop, dados[(j + 13):(j + 15)]])
        j += 15
    return num_routes, newRoutes


class router:
    table = None
    vizinhos = None
    num_routes = 0
    nome_Nodo = None
    #utilizada para criar a tabela globalmen
    def __init__(self,host_name):
        #deque ja tem controle de acesso concorrente a dados
        self.table = deque(maxlen = MAX_ROUTES)
        self.vizinhos = deque(maxlen = MAX_ROUTES)
        self.nome_Nodo = host_name
        
    def cria_tabela(self, viz, lista_conexoes):
         #cria tabela de roteamento
        for item in lista_conexoes:
            self.table.appendleft(item)
            self.num_routes += 1
        #cria lista com os vizinhos
        for item in range(0,len(viz)):
            self.vizinhos.append(item)

    #dada um nova rota atualiza a tabela de roteamento
    def merge_routes (self,new):
        global MUDANCA
        for (i in range(0, self.num_routes)):
            if(new.dest == self.table[i].dest):
                if(new.cost + 1 < int(self.table[i].cost)):
                    in_table = 1
                    break
                else if (new.nexthop == self.nexthop):
                    break
                else:
                    return
        if (i == self.num_routes):
            if (self.num_routes < MAX_ROUTES):
                self.num_routes += 1
                in_table = 0
            else:
                return #tabela ja esta cheia
        #atualiza a tabela de roteamento
        self.table[i] = new
        self.table[i].ttl = MAX_TTL
        self.table[i].cost += 1
        
        #se a rota ja estava na tabela, deleta e depois adiciona a nova, se nao so adiciona
        if (in_table):
            subprocess.call([self.nome_Nodo,"route", "del", "-net", new.dest])
            subprocess.call([self.nome_Nodo,"route", "add", "-net", new.dest, "gw", new.nexthop])
        else:
            subprocess.call([self.nome_Nodo,"route", "add", "-net", new.dest, "gw", new.nexthop])

        
        #COLOCAR O LOCK
        MUDANCA = 1
        self.sendChange()
        #ENVIA O ACK

    def updatingRoutingTable(self,NewRoutes):
        for (i in range(0, len(NewRoutes)):
            self.merge_routes(newRoute[i])
    
                
    def recebeTabela(self, host_name):
        #recebe no modo broadcast
        rs = socket(AF_INET, SOCK_DGRAM)
        end_local=('',54545)
        rs.bind(end_local)
        while (True):
            dados, end_orig = rs.recvfrom(4096)
        
            num_routes, newRoutes = unpack(dados)
            self.updatingRoutingTable(newRoutes)
    
    def enviaTabela(self):
        
        time_to_send_rotina = False
        global MUDANCA, TEMPO_ROTINA
        #LOCK MUDANCA!!!!!!!!!!!!!!!!!!
        t0 = time.time()
        
        while True:
            if ((time.time() - t0) == TEMPO_ROTINA)
                time_to_send_rotina = True
            #se teve uma mudanca ou deu o periodo de enviar o quadro de rotina envia 
            if (MUDANCA or time_to_send_rotina):
                t0 = time.time()
                for item in self.vizinhos:
                    MUDANCA = 0
                    #TIRA O LOCK MUDANCA!!!!!!!
                    dest = item[0]
                    mensagem = ""
                    mensagem += str(self.num_routes)
                    for (j in range(0, num_routes)):
                        #faz o poisoning se tiver mandando a mensagem pro nexthop TEM QUE COLOCAR AQUELES NEGOCIOS DE ZFILL
                        if (dest == self.table[j].nexthop):
                            mensagem += self.table[j].dest
                            mensagem += INFINITO
                        else:
                            mensagem += self.table[j].dest
                            mensagem += self.table[j].cost
                    #envia mensagem
                    item[1].send(mensagem, dest)
                
