import glob
import os

w = 480.0
h = 360.0

from PIL import Image

# Credit Stephen Rauch https://stackoverflow.com/questions/44231209/resize-rectangular-image-to-square-keeping-ratio-and-fill-background-with-black/44231784
def make_square(im, min_size=256, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

for pathAndFilename in glob.iglob(os.path.join("data/train/", "*.txt")):
    s = ""
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title)
    test_image = Image.open('data/train/' + title + '.png')
    new_image = make_square(test_image)
    new_image.save('data/train/' + title + '.png')
    file_train = open('data/train/' + title + '.txt', 'r')
    lines = file_train.readlines()
    for line in lines:
        elements = line.split(" ")
        print(elements)
        x = (float(elements[1]) + (float(elements[3])/2))/w
        y = (60 + float(elements[2]) + (float(elements[4])/2))/w
        width = float(elements[3])/w
        height = float(elements[4])/w
        s += f"0 {x} {y} {width} {height}\n"
    file_train.close()
    print(s)
    file_train = open('data/train/' + title + '.txt', 'w')
    file_train.write(s)
    file_train.close()

for pathAndFilename in glob.iglob(os.path.join("data/test/", "*.txt")):
    s = ""
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title)

    test_image = Image.open('data/test/' + title + '.png')
    new_image = make_square(test_image)
    new_image.save('data/test/' + title + '.png')
    file_train = open('data/test/' + title + '.txt', 'r')
    lines = file_train.readlines()
    for line in lines:
        elements = line.split(" ")
        print(elements)
        x = (float(elements[1]) + (float(elements[3])/2))/w
        y = (60 + float(elements[2]) + (float(elements[4])/2))/w
        width = float(elements[3])/w
        height = float(elements[4])/w
        s += f"0 {x} {y} {width} {height}\n"
    file_train.close()
    print(s)
    file_train = open('data/test/' + title + '.txt', 'w')
    file_train.write(s)
    file_train.close()

