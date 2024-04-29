import os.path

from router import Router
from router_table import RouterTable
from subnet import Subnet
from backbone import BackBone

class FileReader():
    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise FileNotFoundError('File does not exist.')
        self.filename = filename
        
    def get_backbone(self):
        with open(self.filename) as f:
            content = f.readlines()
            
        for current_line, next_line in zip(content, content[1:]):
            current_line = current_line.strip()
            next_line = next_line.strip()
            if current_line == '#SUBNET':
                subnet = self.parse_subnet(next_line)
            elif current_line == "#ROUTER":
                router = self.parse_router(next_line)
            elif current_line == "#ROUTERTABLE":
                router_table = self.parse_router_table(next_line)
            
        return BackBone(subnet=subnet, router=router, router_table=router_table)
    
    def parse_subnet(self, subnet: str):
        subnet = subnet.split(",")
        
        sid          = subnet[0]
        netaddr_mask = subnet[1]
        
        return Subnet(id=sid, netaddr=netaddr_mask)
        
    def parse_router(self, router: str):
        router = router.split(",")
        
        rid      = router[0]
        numifs   = router[1]
        ips_mask = router[2:]
        
        return Router(id=rid, interfaces_num=numifs, ips=ips_mask)
        
    def parse_router_table(self, router_table: str):
        router_table = router_table.split(",")
        
        rid     = router_table[0]
        netaddr = router_table[1]
        nexthop = router_table[2]
        ifnum   = router_table[3]
        
        return RouterTable(id=rid, netaddr=netaddr, next_hop=nexthop, interface_num=ifnum)
        

