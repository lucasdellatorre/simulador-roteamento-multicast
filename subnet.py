from router import Router

class Subnet():
    mainRouter: Router = None

    def __init__(self, id: str, netaddr: str):
        self.id = id
        self.netaddr = netaddr

    def __str__(self):
        string = f'\nsubnet id: {self.id}\n' 
        string = string + f'netaddr/mask: {self.netaddr}'
        string = string + f'\nmain router: {self.mainRouter.id or None}\n'
        return string
    
    def add_main_router(self, router):
        if self.mainRouter is None:
            self.mainRouter = router

    def mjoin(self, groupId: str):
        if self.mainRouter is not None:
            self.mainRouter.mjoin(self.id, groupId)
            print(f'{self.id} => {self.mainRouter.id} : mjoin {groupId};')

    def mleave(self, groupId: str):
        if self.mainRouter is not None:
            self.mainRouter.mleave(self.id, groupId)
            print(f'{self.id} => {self.mainRouter.id} : mleave {groupId};')