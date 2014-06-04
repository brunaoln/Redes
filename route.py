import time

MAX_ROUTES = 64
MAX_TTL = 120 #tempo
INFINITO = 65 #maior que a maxima distancia que um host pode estar do outro
ESPERA_ACK = MAX_TTL/3 # tempo de espera por um ACK
# Nossas mensagens terao como primeiro campo que contem um numero de classificacao da mensagem:
#        0 -> a mensagem eh um ACK
#        1 -> a mensagem eh de rotina
#        2 -> a mensagem eh de mudanca
TAMANHO_MENSAGEM = 1000


class route:
    dest = 0
    nexthop = 0
    cost = 0
    ttl = 0
    def __init__():
        self.dest = 0
        self.nexthop = 0
        self.cost = 0
        self.ttl = 0

class router:
    table = []
    vizinhos = []
    num_routes = 0
    def __init__(viz):
        #cria tabela de roteamento
        for i in range(0, MAX_ROUTES):
            self.table.append(route())
        #cria lista com os vizinhos
        for item in viz:
            self.vizinhos.append(item)
            
    #dada um nova rota atualiza a tabela de roteamento
    def merge_routes (new):
        for (i in range(0, num_routes)):
            if(new.dest == self.table[i].dest):
                if(new.cost + 1 < self.table[i].cost):
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
        self.sendChange()

    def updatingRoutingTable(newRoute, numNewRoutes):
        for (i in range(0, numNewRoutes):
            self.merge_routes(newRoute[i])
    
    def sendChange():
        global INFINITO
        #manda as atualizacoes apenas para os nodos vizinhos
        for (i in range(0, len(self.vizinhos))):
            dest = self.vizinhos[i]
            mensagem = ""
            mensagem += str(2)
            mensagem += str(self.num_routes)
            for (i in range(0, num_routes)):
                #faz o poisoning se tiver mandando a mensagem pro nexthop TEM QUE COLOCAR AQUELES NEGOCIOS DE ZFILL
                if (dest == self.table[i].nexthop):
                    mensagem += self.table[i].dest
                    mensagem += INFINITO
                else:
                    mensagem += self.table[i].dest
                    mensagem += self.table[i].cost
            #envia mensagem
            t = time.time()
            while (recebe = False):
                con_udp.send(mensagem, dest)
                while (time.time() - t <= ESPERA_ACK):
                     msg, addr = con_udp.recvfrom(TAMANHO_MENSAGEM)
                if int(msg[0]) == 0:
                    recebe = True
        
        
