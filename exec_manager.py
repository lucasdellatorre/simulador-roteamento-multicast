from backbone import BackBone

class ExecManager:
    def __init__(self, execution_instructions: list, backbone: BackBone):
        self.execution_instructions = execution_instructions
        self.backbone = backbone
        self.mesagesIdCounter = 0

    def run(self):
        for instruction in self.execution_instructions:
            subnet = self.backbone.findSubnet(instruction.subnet)
            group = instruction.group
            msg = instruction.msg

            if instruction.cmd == 'mjoin':
                subnet.mjoin(group)
            elif instruction.cmd == 'mping':
                subnet.mping(group, msg, self.mesagesIdCounter)
                self.mesagesIdCounter += 1
            elif instruction.cmd == 'mleave':
                subnet.mleave(group)