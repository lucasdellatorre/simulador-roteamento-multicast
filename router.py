from router_table import RouterTableRegistry

class Router():
    def __init__(self, id: str, interfaces_num: int, interfaces: list):
        self.id = id
        self.interfaces = interfaces
        self.interfaces_num = int(interfaces_num)
        self.routerTable = []
        self.groupTable = {}
        
    def __str__(self):
        string = f'\nrouter id: {self.id}' 
        string = string + f'\ninterfaces: {self.interfaces}'
        string = string + f'\nrouter table:'
        for routerTableRegistry in self.routerTable:
            string = string + f'\nregistry: \n{routerTableRegistry}'
        for groupId in self.groupTable:
            string = string + f'\ngroup: {groupId} subnets: {self.groupTable[groupId]}\n'
        return string
    
    def addRouterTableRegistry(self, routerTableRegistry: RouterTableRegistry):
        self.routerTable.append(routerTableRegistry)
    
    def mjoin(self, subNetId: str, groupId: str):
        if groupId not in self.groupTable:
            self.groupTable[groupId] = []
        self.groupTable[groupId].append(subNetId)
        # print(self.groupTable[groupId])
        # print(self.groupTable)

    def mleave(self, subNetId: str, groupId: str):
        if groupId in self.groupTable:
            self.groupTable[groupId].remove(subNetId)
            if len(self.groupTable[groupId]) == 0:
                del self.groupTable[groupId]
                
    def mping(self, groupId: int, msg: str):
        package = {
            "hop": 0,   
            "subnet_src": self.id,
            "group_target": groupId,
            "msg": msg
        }
        
        hasNextRouter: bool = self.interfaces_num > 0
        
        if hasNextRouter:
            self.mflood(package)
            
        if hasNextRouter:
            self.mprune(package)
            
        # ping
        
        print(self.groupTable)
        
        # verifica quantos grupos esse roteador conhece de acordo com suas subnets
        for gId in self.groupTable:
            print("olha o if moco", gId)
            if gId == groupId:
                subnet_messages = ', '.join(f'{self.id} =>> {subnet}' for subnet in self.groupTable[groupId])
                print(f'{subnet_messages} : mping {groupId} {msg};')
        
    # é enviado um pacote de inundação (mflood) entre os roteadores da rede 
    # utilizando RPF para evitar loops
    def mflood(self, package):
        pass
    
    # é enviada uma mensagem mprune para "bloquear" o tráfego multicast
    # de um grupo específico para um roteador
    def mprune(self, package):
        pass

    # quando a mensagem chega na subrede, a mensagem enviada é apresentada (mrecv)
    def mrecv(self):
        pass


        
        