appendMe = '\nNew bit of information'

appendFile = open('exampleFile','a')
appendFile.write(appendMe)
appendFile.close()