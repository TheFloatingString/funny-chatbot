"""
Python script that makes a folder for each of the chapters in the NLTK3 Book
"""

import os

try:
    for i in range(12):
        folderName ='Chapter_'+str(i+1)
        os.makedirs(folderName)


except:
    for i in range(12):
        open('Code_Chapter_'+str(i+1)+'.py','w')
