class Router():
    def __init__(self, id: str, interfaces_num: int, ips: list):
        self.id = id
        self.interfaces_num = interfaces_num
        self.ips = ips
        
    def __str__(self):
        string = "#ROUTER"
        string = string + f'\nrouter id: {self.id}' 
        string = string + f'\ninterfaces count: {self.interfaces_num}'
        for index, ip in enumerate(self.ips):
            string = string + f'\nip{index+1}: {ip}'
        return string