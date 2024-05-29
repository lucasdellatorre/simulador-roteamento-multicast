from router_table import RouterTableRegistry

class Router():
    def __init__(self, id: str, interfaces_num: int, interfaces: list):
        self.id = id
        self.interfaces = interfaces
        self.interfaces_num = interfaces_num
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

    def mleave(self, subNetId: str, groupId: str):
        if groupId in self.groupTable:
            self.groupTable[groupId].remove(subNetId)
            if len(self.groupTable[groupId]) == 0:
                del self.groupTable[groupId]