from file_reader import FileReader
from exec_manager import ExecManager

def main():
    filename = "topologia1.txt"
    backbone = FileReader(filename).get_backbone()
    exec_file_name = "exec.txt"
    exec_instructions = FileReader(exec_file_name).parse_execution_from_exec_file()
    
    exec_manager = ExecManager(exec_instructions, backbone)
    exec_manager.run()
    # print(f'\n{backbone}')
if __name__ == '__main__':
    main()