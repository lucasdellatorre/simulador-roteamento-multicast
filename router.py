from router_table import RouterTableRegistry
# TODO: Mover o mrecv para dentro da subnet, podemos salvar uma referencia para o objeto dentro da groupTable em vez de o id da subnet
class Router():
    def __init__(self, id: str, interfaces_num: int, interfaces: list):
        self.id = id
        self.interfaces = interfaces
        self.interfaces_num = int(interfaces_num)
        self.routerTable = []
        self.groupTable = {}
        self.messagesReceivedDict = {} # {messageId: hopCount}
        self.routersToSendCurrentMessage = []
        
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
                
    def mpingStarter(self, subnetSrcId: int, subnetAddr: str, groupId: int, msg: str, messageId: int):
        package = {
            "hop": 0,   
            "subnet_src": subnetSrcId,
            "subnet_addr": subnetAddr,
            "group_target": groupId,
            "msg": msg,
            "messageId": messageId
        }

        self.messagesReceivedDict[messageId] = 0
        
        hasNextRouter: bool = self.interfaces_num > 0

        if hasNextRouter:
            self.routersToSendCurrentMessage = self.mflood(package)

        self.mping(subnetSrcId, groupId, msg, messageId)

        self.routersToSendCurrentMessage = []

    def mping(self, subnetSrcId: int, groupId: int, msg: str, messageId: int):  
        if self.groupTable.get(groupId) is not None:
            # ping
            subnet_messages = ', '.join(f'{self.id} =>> {subnet}' for subnet in self.groupTable[groupId])
            print(f'{subnet_messages} : mping {groupId} {msg};')    
            self.mrecv(subnetSrcId, groupId, msg)
            
        if len(self.routersToSendCurrentMessage) > 0:    
            router_message = ', '.join(f'{self.id} =>> {router.id}' for router in self.routersToSendCurrentMessage)
            print(f'{router_message} : mping {groupId} {msg};')
            for router in self.routersToSendCurrentMessage:
                router.mping(subnetSrcId, groupId, msg, messageId)


    
    # é enviado um pacote de inundação (mflood) entre os roteadores da rede 
    # utilizando RPF para evitar loops
    def mflood(self, package, receivedFrom=None):
        routers = []
        for routerTableRegistry in self.routerTable:
            # pega da tabela de roteamento apenas os roteadores tirando o que enviou o flood para ele
            if type(routerTableRegistry.next_hop) is Router and routerTableRegistry.next_hop.id != receivedFrom:
                if routerTableRegistry.next_hop not in routers:
                    routers.append(routerTableRegistry.next_hop)
        finalList = routers.copy()
        if len(routers) != 0: 
            router_message = ', '.join(f'{self.id} >> {router.id}' for router in routers)
            print(f'{router_message} : mflood {package["group_target"]};')
            new_package = package.copy()
            new_package["hop"] += 1
            prunedList = []
            # Descobre quais roteadores ignoraram a mensagem dele (RPF) para evitar loops
            # Descobre quais roteadores vão mandar uma mensagem de prune (Na vida real não é assim, mas para o trabalho funciona)
            for i in range(len(routers)):
                value = routers[i].mfloodReceive(new_package, self.id)
                if value == 1: #prune ou ignorado, não repassar
                    finalList.remove(routers[i])
            # Manda os roteadores que sobraram fazer o flood, mesmo os de prune fazem
            for router in finalList:
                isPrune = router.mfloodStart(new_package, self.id)
                if isPrune == False:
                    prunedList.append(router)
            # Remove os roteadores do prune para que eles não recebam a mensagem
            for router in prunedList:
                finalList.remove(router)
                
        return finalList
                
    # Recebe a mensagem de flood e decide o que fazer com ela
    # 0 é prune, 1 é ignorado e 2 é flood aceito e repassado
    def mfloodReceive(self, package, receivedFrom):
        # if package["messageId"] not in self.messagesReceivedDict or package["hop"] < self.messagesReceivedDict[package["messageId"]]:
        if self.findSourceIdInRouterTable(package["subnet_addr"], receivedFrom) == True:
            self.messagesReceivedDict[package["messageId"]] = package["hop"]
            return 2
            # else:
                # print(receivedFrom, self.id)
            # if package["messageId"] not in self.messagesReceivedDict or package["hop"] < self.messagesReceivedDict[package["messageId"]]:
            #     self.messagesReceivedDict[package["messageId"]] = package["hop"]
            #     return 2
            # else:
            #     isSource = self.findSourceIdInRouterTable(package["subnet_src"], receivedFrom)
            #     if isSource == True:
            #         self.messagesReceivedDict[package["messageId"]] = package["hop"]
            #     return 2
        return 1
        
    def findSourceIdInRouterTable(self, sourceId, receivedFrom):
        for routerTableRegistry in self.routerTable:
            # print(routerTableRegistry.netaddr, sourceId, routerTableRegistry.next_hop.id, receivedFrom)
            if routerTableRegistry.netaddr == sourceId and routerTableRegistry.next_hop.id == receivedFrom:
                return True
        return False
            
    def mfloodStart(self, package, receivedFrom):
        self.routersToSendCurrentMessage = self.mflood(package, receivedFrom)
        if package["group_target"] not in self.groupTable and len(self.routersToSendCurrentMessage) == 0:
            self.mprune(receivedFrom, package["group_target"])
            return False
        return True
    
    # é enviada uma mensagem mprune para "bloquear" o tráfego multicast
    # de um grupo específico para um roteador
    def mprune(self, sendTo, groupId):
        print(f'{self.id} >> {sendTo} : mprune {groupId};')

    # quando a mensagem chega na subrede, a mensagem enviada é apresentada (mrecv)
    def mrecv(self, subnetSrcId: int, groupId: int, msg: str):
        for subnetId in self.groupTable[groupId]:
            print(f'{subnetId} box {subnetId} : {groupId}#{msg} from {subnetSrcId};')
            
            
        
                
                