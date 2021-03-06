import numpy as np
import cv2
import os
#import re
#import fnmatch
# ???

# recurse into every directory that has images that match filename pattern
# build data format:
# path and filename, flattened array of image data, command
#
# Each image will be 259200 bytes or just about 1/4 MB
# This might be necessary if we decide to train on large batches.

print(os.getcwd())

#imgdir = './'
imgdir = "img_dir"

# we are going to only go one level down on subdirectories
#subdirs = os.listdir('./') # Guess I need a list comprehension thingie?
subdirs = [dirs for dirs in os.listdir(imgdir) if os.path.isdir(dirs)]
print(subdirs)
# TODO make safer, like how current structure has nested directory

# print(os.listdir(subdirs[0])) # forgot to put files in the first directory

training_data = []

#training_data[0] = "dir/file.png"
#training_data[1] = "123456"
#training_data[2] = "FS"

def flattenImage(path):
    # take in path to image and return flattened numpy array
    # TODO make safer
    # return np.array(cv2.imread(path)).flatten()
    #
    # perform our deinterlace and shrink
    img = cv2.imread(path)
    img = img[0::2,0::2,::] # now deinterlaced and shrunk
    return np.array(img).flatten()
    

def getDirection(filename):
    # TODO make safer with a regexp or something
    # assuming 3 letter extension with .
    #print(filename[-6:-4])
    return filename[-6:-4]
    
for s in subdirs:
    # files = [filz for filz in os.listdir(s)] # if fnmatch.fnmatch(filz, '^[01234567890.]{10,13}\-[\w]{0,64}\-[FNB][LSR].png$')]
    files = os.listdir(s)
    # if the trick works, why not do it twice?
    # if it doesn't work, then let's not do it...
    for fi, f in enumerate(files):
        # Have to be careful to not delete from list we're iterating over
        d = [s + "/" + f,
             flattenImage(s + "/" + f),
             getDirection(f)]
        #d = []
        #d[0] = s + "/" + f
        #d[1] = "123" # flattened image
        #d[2] = "FS"
        training_data.append(d) # add row
        # path may not be portable

#print(training_data[0])
for td in training_data:
    print(td)
#    for t in td[1]:
#        print(t)
# make sure we have some valid data
