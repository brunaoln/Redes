import time
from collections import deque
from socket import *

MAX_ROUTES = 64
MAX_TTL = 120 #tempo
INFINITO = 65 #maior que a maxima distancia que um host pode estar do outro
ESPERA_ACK = MAX_TTL/3 # tempo de espera por um ACK
MUDANCA = 0

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
    num_routes = int(dados[1:3])
    newRoutes = []
    j = 3
    for (i in range (0, num_routes)):
        #cria rotas com os dados do pacote
        newRoutes.append(route(j:(j + 14)], nexthop, dados[(j + 14):(j + 16)]])
        j += 16
    return num_routes, newRoutes


class router:
    table = None
    vizinhos = []
    conexoes = None
    num_routes = 0
    #utilizada para criar a tabela globalmen
    def __init__():
        #deque ja tem controle a acesso concorrente de dados
        table = deque(maxlen = MAX_ROUTES)
        
    def cria_tabela(viz, lista_conexoes):
         #cria tabela de roteamento
        for item in lista_conexoes:
            self.table.appendleft(item)
            self.num_routes += 1
        #cria lista com os vizinhos
        for item in viz:
            self.vizinhos.append(item)
        self.conexoes = lista_conexoes
        
    #dada um nova rota atualiza a tabela de roteamento
    def merge_routes (new):
        global MUDANCA
        for (i in range(0, self.num_routes)):
            if(new.dest == self.table[i].dest):
                if(new.cost + 1 < int(self.table[i].cost)):
                    break
                else if (new.nexthop == self.nexthop):
                    break
                else:
                    return
        if (i == num_routes):
            if (num_routes < MAX_ROUTES):
                num_routes += 1
            else:
                return #tabela ja esta cheia
        #atualiza a tabela de roteamento
        self.table[i] = new
        self.table[i].ttl = MAX_TTL
        self.table[i].cost += 1
        
        #COLOCAR O LOCK
        MUDANCA = 1
        self.sendChange()
        #ENVIA O ACK

    def updatingRoutingTable(NewRoutes):
        for (i in range(0, len(NewRoutes)):
            self.merge_routes(newRoute[i])
    
    def sendChange(num_routes, rotas):
        global INFINITO
        #manda as atualizacoes apenas para os nodos vizinhos
        for (i in range(0, len(self.vizinhos))):
            dest = self.vizinhos[i]
            mensagem = ""
            mensagem += str(3)
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
            t = time.time()
            recebe = False
            numero_tentativas = 0
            while (recebe is False and numero_tentativas < MAXIMO_NUMERO_TENTATIVAS):
                self.conecoes[i].send(mensagem, dest)
                while (time.time() - t <= ESPERA_ACK):
                     msg, addr = self.conexoes[i].recvfrom(TAMANHO_MENSAGEM)
                if int(msg[0]) == 0:
                    recebe = True
                else:
                    numero_tentativas += 1
            if numero_tentativas == MAXIMO_NUMERO_TENTATIVAS:
                #atualiza todas as entradas que tenham esse nó de destino incomunicável com distâncias iguais a INFINITO 
                
    def recebeTabela():
        #recebe no modo broadcast
        rs = socket(AF_INET, SOCK_DGRAM)
        end_local=('',54545)
        rs.bind(end_local)
        while (True):
            dados, end_orig = rs.recvfrom(4096)
        
            num_routes, newRoutes = unpack(dados)
            self.updatingRoutingTable(newRoutes) 
            
