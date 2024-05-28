class RouterTableRegistry():
    def __init__(self, netaddr: str, next_hop: str, interface_num: int):
        self.netaddr = netaddr
        self.next_hop = next_hop
        self.interface_num = interface_num
        
    def __str__(self):
        string = f'netaddr/mask: {self.netaddr}\n'
        string = string + f'next hop: {self.next_hop}\n'
        string = string + f'interface count: {self.interface_num}'
        return string
    