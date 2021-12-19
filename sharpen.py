import cv2
import numpy as np
import glob, os

#Sharpening training set
for pathAndFilename in glob.iglob(os.path.join("data/train/", "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title)
    image = cv2.imread('data/train/' + title + '.png')
    kernel = np.array([[-1,-1,-1], 
                        [-1, 9,-1],
                        [-1,-1,-1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    cv2.imwrite(os.path.join("sharpened_train", title+'.png'),sharpened)

#Sharpening testing set
for pathAndFilename in glob.iglob(os.path.join("testnew/", "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title)
    image = cv2.imread('testnew/' + title + '.png')
    kernel = np.array([[-1,-1,-1], 
                        [-1, 9,-1],
                        [-1,-1,-1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    cv2.imwrite(os.path.join("sharpened_testnew", title+'.png'),sharpened)

#Sharpening validation set
for pathAndFilename in glob.iglob(os.path.join("valnew/", "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title)
    image = cv2.imread('valnew/' + title + '.png')
    kernel = np.array([[-1,-1,-1], 
                        [-1, 9,-1],
                        [-1,-1,-1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    cv2.imwrite(os.path.join("sharpened_valnew", title+'.png'),sharpened)
