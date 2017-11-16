text = 'Munaf \n Sample Text'

saveFile=open('exampleFie.txt','w')
saveFile.write(text)
saveFile=open('exampleFie.txt','r')
text=saveFile.read()

print(text)
saveFile.close()

