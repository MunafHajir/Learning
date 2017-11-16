import os

#uncomment to get current directory

curDir = os.getcwd()

print(curDir)

os.mkdir('munafDir')

import time
time.sleep(2)

os.rename('munafDir','newDir')
time.sleep(2)

os.rmdir('newDir')