import random
from shutil import copyfile
import glob, os
import cv2

images = glob.glob("data/test/*.png")
labels = glob.glob("data/test/*.txt")
c = list(zip(images, labels))

random.shuffle(c)

images, labels = zip(*c)
#print (images)
#print (labels)
#print('data/test\\0067.png'.split("\\"))

i=0
for label in labels:
    #cv2.save(path)
    pathtofile = (label.split("\\")[0])
    filename = (label.split("\\")[1]) #0067
    filenamenoformat = filename.split(".")[0] #0067

    if (i<=124): 
        copyfile (pathtofile + "/" + filename, 'testnew/' + filenamenoformat+".txt" )
        copyfile (pathtofile +  "/" + filename, 'testnew/' + filenamenoformat+".png" )
    else: 
        copyfile(pathtofile +  "/" + filename, 'valnew/' + filenamenoformat + ".txt")
        copyfile (pathtofile +  "/" + filename, 'valnew/' + filenamenoformat+".png" )
    i+=1