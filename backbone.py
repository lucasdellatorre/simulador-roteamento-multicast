class BackBone():
    def __init__(self, subnets: list, routers: list):
        self.subnets = subnets
        self.routers = routers
    
    def __str__(self):
        string = '#SUBNET\n'
        for subnet in self.subnets:
            string = string + f'{subnet}\n'
        string = string + '#ROUTER\n'
        for router in self.routers:
            string = string + f'{router}\n'
        return string
    
    def findSubnet(self, subnetId: str):
        for subnet in self.subnets:
            if subnet.id == subnetId:
                return subnet
        return None
