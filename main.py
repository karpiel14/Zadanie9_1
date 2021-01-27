try:
    with open("file1.txt", 'r') as file1:
        with open("file2.txt", 'w') as file2:
            for linia in file1:
                file2.write(linia)
except IOError as ioe:
    print("Error {}".format(ioe))