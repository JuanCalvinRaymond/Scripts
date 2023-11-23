from sys import argv
import os

cwd = os.getcwd()

#Create a folder and move the files into that folder
if len(argv) > 1:
    filelist = os.listdir(argv[1])
    for file in filelist:
        print(file)
        fileextention = file.split(".", 1)
        if fileextention[1] == "jfif":
            fileextention[1] = "jpeg"
            newName = fileextention[0] + "." + fileextention[1]
            print('Renaming to new format: ' + newName)
            os.rename(argv[1] + "\\" + file, argv[1] + "\\" + newName)
