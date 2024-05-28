from backbone import BackBone

class ExecManager:
    def __init__(self, execution_instructions: list, backbone: BackBone):
        self.execution_instructions = execution_instructions
        self.backbone = backbone

    def run(self):
        for instruction in self.execution_instructions:
            subnet = self.backbone.findSubnet(instruction.subnet)
            group = instruction.group

            if instruction.cmd == 'mjoin':
                subnet.mjoin(group)
            elif instruction.cmd == 'mping':
                print(f'Pinging {subnet.id} to {group}')
            elif instruction.cmd == 'mleave':
                print(f'Leaving {group} from {subnet.id}')