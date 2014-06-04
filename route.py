MAX_ROUTES = 128
MAX_TTL = 120 #tempo

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
        #tem que setar uma variavel falando que vai enviar a nova rota ou eviar por aqui mesmo
    
    def updatingRoutingTable(newRoute, numNewRoutes):
        for (i in range(0, numNewRoutes):
            self.merge_routes(newRoute[i])
    
        
        
