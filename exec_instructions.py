class ExecInstructions():
    def __init__(self, cmd, subnet, group, msg):
        self.cmd = cmd
        self.subnet = subnet
        self.group = group
        self.msg = msg
    
    def __str__(self):
        return f'{self.cmd} {self.subnet} {self.group} {self.msg}'