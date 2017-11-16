appendMe='New Bit of information'

appendFile=open('exampleFie.txt','a')

appendFile.write('\n')
appendFile.write(appendMe)

appendFile.close()