import cv2
import numpy as np
import glob, os

def increase_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

#image = cv2.imread('data/test/0001.png')
#frame = increase_brightness(image, value=120)
#cv2.imshow('Image Sharpening', frame)
#cv2.waitKey(0)

# Brightening testing set
for pathAndFilename in glob.iglob(os.path.join("testnew/", "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title)
    image = cv2.imread('testnew/' + title + '.png')
    brightened = increase_brightness(image, value=120)
    cv2.imwrite(os.path.join("brightened_test", title+'.png'),brightened)

# Brightening validation set
for pathAndFilename in glob.iglob(os.path.join("valnew/", "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title)
    image = cv2.imread('valnew/' + title + '.png')
    brightened = increase_brightness(image, value=120)
    cv2.imwrite(os.path.join("brightened_val", title+'.png'),brightened)

# Brightening training set
for pathAndFilename in glob.iglob(os.path.join("data/train/", "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title)
    image = cv2.imread('data/train/' + title + '.png')
    brightened = increase_brightness(image, value=120)
    cv2.imwrite(os.path.join("brightened_train", title+'.png'),brightened)




