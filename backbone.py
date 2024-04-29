class BackBone():
    def __init__(self, subnet, router, router_table):
        self.subnet = subnet
        self.router = router
        self.router_table = router_table
    
    def __str__(self):
        return f'{self.subnet}\n{self.router}\n{self.router_table}'