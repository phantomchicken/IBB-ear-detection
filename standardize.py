# example of global centering (subtract mean)
import numpy as np
from numpy import asarray
from PIL import Image
import glob, os
import cv2

for pathAndFilename in glob.iglob(os.path.join("data/test/", "*.txt")):

    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title)
    image = Image.open('data/test/' + title + '.png')
    pixels = asarray(image)
    
    pixels = pixels.astype('float32') # convert from integers to floats
    mean, std = pixels.mean(), pixels.std()  # calculate global mean and standard deviation
    print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
    
    pixels = (pixels - mean) / std 
    mean, std = pixels.mean(), pixels.std() # confirm it had the desired effect
    print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
    
    #cv2.imwrite(os.path.join("standardized_test", title+'.png'),pixels)
    #im = Image.fromarray(pixels)
    im = Image.fromarray((pixels * 255).astype(np.uint8))
    im.save("standardized_test/"+title+".png")

for pathAndFilename in glob.iglob(os.path.join("data/train/", "*.txt")):

    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title)
    image = Image.open('data/train/' + title + '.png')
    pixels = asarray(image)
    
    pixels = pixels.astype('float32') # convert from integers to floats
    mean, std = pixels.mean(), pixels.std()  # calculate global mean and standard deviation
    print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
    
    pixels = (pixels - mean) / std 
    mean, std = pixels.mean(), pixels.std() # confirm it had the desired effect
    print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
    
    #cv2.imwrite(os.path.join("standardized_test", title+'.png'),pixels)
    #im = Image.fromarray(pixels)
    im = Image.fromarray((pixels * 255).astype(np.uint8))
    im.save("standardized_train/"+title+".png")