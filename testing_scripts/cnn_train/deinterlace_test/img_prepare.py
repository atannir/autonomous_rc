import cv2
import numpy as np

# load image, skip every other line (starting with 0 or 1?)
# skip every other pixel to reduce size again
# flatten image to prepare for insertion to convolutional neural network

# 1518386449.51-demo1-FR.png
# 1518386452.33-demo1-FR.png
# 1518386454.33-demo1-FR.png

#filename = "1518386449.51-demo1-FR.png"
#filename = "1518386452.33-demo1-FR.png"
filename = "1518386454.33-demo1-FR.png"

img = cv2.imread(filename)
print("Size: " + str(img.size))
print("Shape: " + str(img.shape))
print(str(img[400][700][2]))

img_even = img[0::2][::][::]
img_odd = img[1::2][::][::]
# [][][] syntax did not work, but [,,] did
img_skip = img[0::2,0::2,::]
img_skip2 = img[1::2,0::2,::]
print("Size: " + str(img_even.size))
print("Shape: " + str(img_even.shape))
print("Size: " + str(img_odd.size))
print("Shape: " + str(img_odd.shape))
print("Size: " + str(img_skip.size))
print("Shape: " + str(img_skip.shape))
cv2.imwrite("even_" + filename, img_even)
cv2.imwrite("odd_" + filename, img_odd)
cv2.imwrite("skip_" + filename, img_skip)
cv2.imwrite("skip2_" + filename, img_skip2) # worse from samples tested
