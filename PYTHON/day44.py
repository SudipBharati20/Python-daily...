def read_file(path, mode):
    file=open(path,mode)
    print(file.read())
    file.close()
read_file('file.txt','r')
read_file('password.txt','a')
