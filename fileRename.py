import os
import shutil

dir = os.getcwd()

networkPath = '\\\\MysharedFolder\\SubFolder\\Files and Folders to Process\\'
def readDirectory(dir):
    for filename in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, filename)):
            readDirectory(os.path.join(dir, filename)) # recursive
        
        if filename.count('.') > 1 and not os.path.isdir(os.path.join(dir, filename)):
            newName = filename.replace('.', '_', filename.count('.') - 1)
            print(filename + "-->"+ newName)
            os.rename(os.path.join(dir, filename), os.path.join(dir, newName))

readDirectory(networkPath)