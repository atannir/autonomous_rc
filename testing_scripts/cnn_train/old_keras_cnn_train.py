import numpy as np
import cv2
import os

#from keras.models import Sequential
#from keras.preprocessing.image import array_to_img, img_to_array, load_img
#from keras.layers import Activation, Conv2D, MaxPooling2D, Flatten, Dense

# for each training directory in curated set
# open image, extract direction from filename
# run and store completed model

# This model is based on roughly the one used in NVidia's DAVE-2
# project, although with fewer layers and larger image size

imgdir = "curated" # local directory or path

subdirs = [dirs for dirs in os.listdir(imgdir)] #if os.path.isdir(dirs)]
# worked before in test script, won't work here. :-\
# TODO fix this so we are not messing with files that are not images

#print(subdirs)

# build data from image sets

training_data = []

def flattenImage(path):
    # TODO make safer
    img = cv2.imread(path)
    img = img[0::2,0::2,::] # now deinterlaced and shrunk
    return np.array(img).flatten()


def getDirection(filename):
    # TODO make safer with a regexp or something
    return filename[-6:-4]


# build dataset from all images
# may need to watch out for memory later
for s in subdirs:
    print(s)
    #files = os.listdir(s)
#    print(files)
