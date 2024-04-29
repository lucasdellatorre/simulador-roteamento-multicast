class RouterTable():
    def __init__(self, id: str, netaddr: str, next_hop: str, interface_num: int):
        self.id = id
        self.netaddr = netaddr
        self.next_hop = next_hop
        self.interface_num = interface_num
        
    def __str__(self):
        string = "#ROUTERTABLE\n"
        string = string + f'router table id: {self.id}\n' 
        string = string + f'netaddr/mask: {self.netaddr}\n'
        string = string + f'next hop: {self.next_hop}\n'
        string = string + f'interface count: {self.interface_num}'
        return string
        