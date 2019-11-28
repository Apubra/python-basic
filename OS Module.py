# Sample code using os:
import os
curDir = os.getcwd()
print(curDir)


# To make a new directory:
os.mkdir('newDir')

# To change the name of, or rename, a directory:
os.rename('newDir','newDir2')


# To remove a directory:
os.rmdir('newDir2')


# /////////////////////////////////Advance//////////////////////
# import os

# # define the name of the directory to be created
# path = "/root/tmp/year"

# try:
#     os.mkdir(path)
# except OSError:
#     print ("Creation of the directory %s failed" % path)
# else:
#     print ("Successfully created the directory %s " % path)

# import os

# # define the name of the directory to be created
# path = "/root/year/month/week/day"

# try:
#     os.makedirs(path)
# except OSError:
#     print ("Creation of the directory %s failed" % path)
# else:
#     print ("Successfully created the directory %s" % path)


# import tempfile

# # create a temporary directory
# with tempfile.TemporaryDirectory() as directory:
#     print('The created temporary directory is %s' % directory)

# # directory and its contents have been removed by this point


# import os
# import shutil
# # define the name of the directory to be deleted
# path = "/root/Desktop/year/month/week/day/"

# try:
#     # shutil.rmtree(path)
#     os.rmdir(path)
# except OSError:
#     print ("Deletion of the directory %s failed" % path)
# else:
#     print ("Successfully deleted the directory %s" % path)


# ///////////////////////////////////////////////////////////////
'''
mkdir vs makedirs
mkdir- can makes one directory
makedirs- can makes multiple directory

shutil.rmtree(path) vs os.rmdir(path)
os.rmdir(path)- can delete only directory not in directory property
shutil.rmtree(path)-can delete directory and in directory property
'''