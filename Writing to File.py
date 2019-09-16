# Basic parameter for file is read, write and open
text = 'Sample Text to Save\nNew line!'

saveFile = open('exampleFile','w')
saveFile.write(text)
saveFile.close()