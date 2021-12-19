import cv2
import numpy as np
import glob, os

# Credit Mitch McMabers https://stackoverflow.com/questions/25349178/calculating-percentage-of-bounding-box-overlap-for-image-detector-evaluation
def get_iou(bb1, bb2):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.

    Parameters
    ----------
    bb1 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x1, y1) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner
    bb2 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x, y) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner

    Returns
    -------
    float
        in [0, 1]
    """
    assert bb1['x1'] < bb1['x2']
    assert bb1['y1'] < bb1['y2']
    assert bb2['x1'] < bb2['x2']
    assert bb2['y1'] < bb2['y2']

    # determine the coordinates of the intersection rectangle
    x_left = max(bb1['x1'], bb2['x1'])
    y_top = max(bb1['y1'], bb2['y1'])
    x_right = min(bb1['x2'], bb2['x2'])
    y_bottom = min(bb1['y2'], bb2['y2'])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box
    intersection_area = (x_right - x_left) * (y_bottom - y_top)

    # compute the area of both AABBs
    bb1_area = (bb1['x2'] - bb1['x1']) * (bb1['y2'] - bb1['y1'])
    bb2_area = (bb2['x2'] - bb2['x1']) * (bb2['y2'] - bb2['y1'])

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
    return iou

# Normal set calculation
globalIOU = 0
ct=0
for pathAndFilename in glob.iglob(os.path.join("testnew/", "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    #print(pathAndFilename)
    coordinates = []
    fileGT = open(pathAndFilename)
    linesGT = fileGT.readlines()
    
    file = open('exp6/labels/' + title + '.txt', 'r')
    lines = file.readlines()

    for line in linesGT:
        elements = line.split(" ")
        x1gt = ((float(elements[1]) - float(elements[3])/2.0) * 480)
        y1gt = ((float(elements[2]) - float(elements[4])/2.0) * 480)
        x2gt = ((float(elements[1]) + float(elements[3])/2.0) * 480)
        y2gt = ((float(elements[2]) + float(elements[4])/2.0) * 480)
        elements = elements[1:]
        elements = [float(i) for i in elements]
        dict1 = {"x1": x1gt, 'x2': x2gt, 'y1': y1gt, 'y2': y2gt}
        #print(elements)
        #coordinates.append(linesGT)
        #print(len(lines))
    for line2 in lines:
        elements2 = line2.split(" ")
        x1 = ((float(elements2[1]) - float(elements2[3])/2.0) * 480)
        y1 = ((float(elements2[2]) - float(elements2[4])/2.0) * 480)
        x2 = ((float(elements2[1]) + float(elements2[3])/2.0) * 480)
        y2 = ((float(elements2[2]) + float(elements2[4])/2.0) * 480)
        elements2 = elements2[1:]
        elements2 = elements2[:-1]
        elements2 = [float(i) for i in elements2]
        dict2 = {"x1": x1, 'x2': x2, 'y1': y1, 'y2': y2}
        #print(elements2)

    if (len(linesGT)>len(lines)):
        print("FN")
    elif(len(linesGT)<len(lines)):
        print("FP")
    else:
        iou = get_iou(dict1, dict2)
        globalIOU += iou
        ct+=1

print("IOU for normal set ", globalIOU/ct)

# Sharpened set calculation
globalIOU = 0
ct=0
for pathAndFilename in glob.iglob(os.path.join("testnew/", "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    coordinates = []
    fileGT = open(pathAndFilename)
    linesGT = fileGT.readlines()
    
    file = open('exp5/labels/' + title + '.txt', 'r')
    lines = file.readlines()
    
    for line in linesGT:
        elements = line.split(" ")
        x1gt = ((float(elements[1]) - float(elements[3])/2.0) * 480)
        y1gt = ((float(elements[2]) - float(elements[4])/2.0) * 480)
        x2gt = ((float(elements[1]) + float(elements[3])/2.0) * 480)
        y2gt = ((float(elements[2]) + float(elements[4])/2.0) * 480)
        elements = elements[1:]
        elements = [float(i) for i in elements]
        dict1 = {"x1": x1gt, 'x2': x2gt, 'y1': y1gt, 'y2': y2gt}

    for line2 in lines:
        elements2 = line2.split(" ")
        x1 = ((float(elements2[1]) - float(elements2[3])/2.0) * 480)
        y1 = ((float(elements2[2]) - float(elements2[4])/2.0) * 480)
        x2 = ((float(elements2[1]) + float(elements2[3])/2.0) * 480)
        y2 = ((float(elements2[2]) + float(elements2[4])/2.0) * 480)
        elements2 = elements2[1:]
        elements2 = elements2[:-1]
        elements2 = [float(i) for i in elements2]
        dict2 = {"x1": x1, 'x2': x2, 'y1': y1, 'y2': y2}

    if (len(linesGT)>len(lines)):
        print("FN")
    elif(len(linesGT)<len(lines)):
        print("FP")
    else:
        iou = get_iou(dict1, dict2)
        globalIOU += iou
        ct+=1

print("IOU for sharpened set ", globalIOU/ct)

# Brightened set calculation
globalIOU = 0
ct=0
for pathAndFilename in glob.iglob(os.path.join("testnew/", "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    coordinates = []
    fileGT = open(pathAndFilename)
    linesGT = fileGT.readlines()
    
    file = open('exp6/labels/' + title + '.txt', 'r')
    lines = file.readlines()
    
    for line in linesGT:
        elements = line.split(" ")
        x1gt = ((float(elements[1]) - float(elements[3])/2.0) * 480)
        y1gt = ((float(elements[2]) - float(elements[4])/2.0) * 480)
        x2gt = ((float(elements[1]) + float(elements[3])/2.0) * 480)
        y2gt = ((float(elements[2]) + float(elements[4])/2.0) * 480)
        elements = elements[1:]
        elements = [float(i) for i in elements]
        dict1 = {"x1": x1gt, 'x2': x2gt, 'y1': y1gt, 'y2': y2gt}
    for line2 in lines:
        elements2 = line2.split(" ")
        x1 = ((float(elements2[1]) - float(elements2[3])/2.0) * 480)
        y1 = ((float(elements2[2]) - float(elements2[4])/2.0) * 480)
        x2 = ((float(elements2[1]) + float(elements2[3])/2.0) * 480)
        y2 = ((float(elements2[2]) + float(elements2[4])/2.0) * 480)
        elements2 = elements2[1:]
        elements2 = elements2[:-1]
        elements2 = [float(i) for i in elements2]
        dict2 = {"x1": x1, 'x2': x2, 'y1': y1, 'y2': y2}

    if (len(linesGT)>len(lines)):
        print("FN")
    elif(len(linesGT)<len(lines)):
        print("FP")
    else:
        iou = get_iou(dict1, dict2)
        globalIOU += iou
        ct+=1

print("IOU for brightened set ", globalIOU/ct)

# Standardized set calculation
globalIOU = 0
ct=0
for pathAndFilename in glob.iglob(os.path.join("testnew/", "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    coordinates = []
    fileGT = open(pathAndFilename)
    linesGT = fileGT.readlines()
    
    file = open('exp7/labels/' + title + '.txt', 'r')
    lines = file.readlines()
    
    for line in linesGT:
        elements = line.split(" ")
        x1gt = ((float(elements[1]) - float(elements[3])/2.0) * 480)
        y1gt = ((float(elements[2]) - float(elements[4])/2.0) * 480)
        x2gt = ((float(elements[1]) + float(elements[3])/2.0) * 480)
        y2gt = ((float(elements[2]) + float(elements[4])/2.0) * 480)
        elements = elements[1:]
        elements = [float(i) for i in elements]
        dict1 = {"x1": x1gt, 'x2': x2gt, 'y1': y1gt, 'y2': y2gt}
    for line2 in lines:
        elements2 = line2.split(" ")
        x1 = ((float(elements2[1]) - float(elements2[3])/2.0) * 480)
        y1 = ((float(elements2[2]) - float(elements2[4])/2.0) * 480)
        x2 = ((float(elements2[1]) + float(elements2[3])/2.0) * 480)
        y2 = ((float(elements2[2]) + float(elements2[4])/2.0) * 480)
        elements2 = elements2[1:]
        elements2 = elements2[:-1]
        elements2 = [float(i) for i in elements2]
        dict2 = {"x1": x1, 'x2': x2, 'y1': y1, 'y2': y2}

    if (len(linesGT)>len(lines)):
        print("FN")
    elif(len(linesGT)<len(lines)):
        print("FP")
    else:
        iou = get_iou(dict1, dict2)
        globalIOU += iou
        ct+=1

print("IOU for standardized set ", globalIOU/ct)