from backbone import BackBone

class ExecManager:
    def __init__(self, execution_instructions: list, backbone: BackBone):
        self.execution_instructions = execution_instructions
        self.backbone = backbone

    def run(self):
        for instruction in self.execution_instructions:
            subnet = self.backbone.findSubnet(instruction.subnet)
            group = instruction.group
            msg = instruction.msg

            if instruction.cmd == 'mjoin':
                subnet.mjoin(group)
            elif instruction.cmd == 'mping':
                subnet.mping(group, msg)
            elif instruction.cmd == 'mleave':
                subnet.mleave(group)