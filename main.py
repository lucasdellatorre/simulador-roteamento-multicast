from file_reader import FileReader

def main():
    filename = "topologia.txt"
    backbone = FileReader(filename).get_backbone()
    print(backbone)
    
if __name__ == '__main__':
    main()