from file_reader import FileReader
from exec_manager import ExecManager
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <topologia.txt> <exec.txt>")
        sys.exit(1)
    
    filename = sys.argv[1]
    backbone = FileReader(filename).get_backbone()
    exec_file_name = sys.argv[2]
    exec_instructions = FileReader(exec_file_name).parse_execution_from_exec_file()
    
    exec_manager = ExecManager(exec_instructions, backbone)
    exec_manager.run()
    # print(f'\n{backbone}')    
if __name__ == '__main__':
    main()