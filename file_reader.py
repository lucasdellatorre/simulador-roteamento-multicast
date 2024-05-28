import os.path
from typing import Set

from router import Router
from router_table import RouterTableRegistry
from subnet import Subnet
from backbone import BackBone
from exec_instructions import ExecInstructions

class FileReader():
    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise FileNotFoundError('File does not exist.')
        self.filename = filename
        
    def get_backbone(self):
        with open(self.filename) as f:
            content = f.readlines()
    
        subnets = []
        routers = []

        registers = ['#SUBNET', '#ROUTER', '#ROUTERTABLE']
        current_registering = []
        for index in range(len(content)):
            current_line = content[index].strip()
            if registers.__contains__(current_line):
                current_registering = current_line
            elif current_registering == '#SUBNET':
                subnets.append(self.parse_subnet(current_line))
            elif current_registering == "#ROUTER":
                routers.append(self.parse_router(current_line))
            elif current_registering == "#ROUTERTABLE":
                self.parse_router_table(current_line, routers, subnets)
            
        return BackBone(subnets, routers)
    
    def parse_subnet(self, subnet: str):
        subnet = subnet.split(",")
        
        sid          = subnet[0]
        netaddr_mask = subnet[1]
        
        return Subnet(id=sid, netaddr=netaddr_mask)
        
    def parse_router(self, router: str):
        router = router.split(",")
        
        rid      = router[0]
        numifs = router[1]
        interfaces = router[2:]
        
        return Router(id=rid, interfaces_num=numifs, interfaces=interfaces)
        
    def parse_router_table(self, table_line, router_list, subnet_list):
        router = None
        table_line = table_line.strip().split(",")
        for rtr in router_list:
            if rtr.id == table_line[0]:
                router = rtr
                break

        
        netaddr = table_line[1]
        nexthop = table_line[2]
        ifnum   = table_line[3]
        
        router.addRouterTableRegistry(RouterTableRegistry(netaddr=netaddr, next_hop=nexthop, interface_num=ifnum))

        if nexthop.__contains__('0.0.0.0'):
            for subnet in subnet_list:
                if subnet.netaddr == netaddr:
                    subnet.add_main_router(router)
                    break
    
    def parse_execution_from_exec_file(self):
        with open(self.filename) as f:
            content = f.readlines()
        instructions = []

        for line in content:
            line = line.strip().split(' ')
            instructions.append(ExecInstructions(line[0], line[1], line[2], line[3] if len(line) > 3 else None))
            
        return instructions
        

