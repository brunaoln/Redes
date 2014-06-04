MAX_ROUTES = 127
MAX_TTL = 120 #tempo
INFINITO = 128 #maior que a maxima distancia que um host pode estar do outro

def route:
    dest = 0
    nexthop = 0
    cost = 0
    ttl = 0
    def __init__():
        self.dest = 0
        self.nexthop = 0
        self.cost = 0
        self.ttl = 0

def router:
    table = []
    num_routes = 0
    def __init__():
        for i in range(0, MAX_ROUTES):
            table.append(route())
            
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
        #TEM QUE MUDAR PRA SOH MANDAR PRO VIZINHOS, ACHO QUE TEM QUE CRIAR UMA LISTA DE VIZINHOS
        for (i in range(0, num_routes)):
            dest = self.nexthop
            mensagem = ""
            mensagem += str(self.num_routes)
            for (i in range(0, num_routes)):
                #faz o poisoning se tiver mandando a mensagem pro nexthop
                if (dest == self.table[i].nexthop):
                    mensagem += self.table[i].dest
                    mensagem += INFINITO
                else:
                    mensagem += self.table[i].dest
                    mensagem += self.table[i].cost
            #envia mensagem
            send(mensagem, destino)
    
        
        
