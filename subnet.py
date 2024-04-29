class Subnet():
    def __init__(self, id: str, netaddr: str):
        self.id = id
        self.netaddr = netaddr
        
    def __str__(self):
        string = "#SUBNET\n"
        string = string + f'subnet id: {self.id}\n' 
        string = string + f'netaddr/mask: {self.netaddr}'
        return string