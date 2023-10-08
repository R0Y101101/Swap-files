def swapFileData():
    file1 = input("Enter files name:")
    file2 = input("Enter files name:")

    with open(file1,"r") as a:
        data_a = a.read()

    with open(file1,"r") as b:
        data_b = b.read()

    with open(file1,"w") as a:
        a.write = a.write()

    with open(file1,"w") as b:
        b.write = b.write()

swapFileData()