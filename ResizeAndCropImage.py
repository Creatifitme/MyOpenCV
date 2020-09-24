import cv2
import numpy as np

# RESIZE AND CROP IMAGE
# RESIZE PICTURE / IMAGE
path2 = "Resources/road.jpg"

img2 = cv2.imread(path2)

# print/diplay the "ACTUAL IMAGE SIZE".
# Result is (800, 1200, 3) means the height (Y) is 800 and width (X) is 1200
# picture has 3 COLOR channels
# in opencv: the positive X axis is from left (0,0 coordinate) to right
#            the positive Y axis is from top (0,0 coordinate) to bottom (not from bottom 0,0 coordinate to top like normal "Y axis")
print(img2.shape)

cv2.imshow("The Road Pict",img2)

# resize the width and height of a picture to whatever size we like
# can also resize to bigger width and height (then the original picture) but NO INCREASE THE PICT QUALITY
custom_width = 400
custom_height = 400
imgResize = cv2.resize(img2,(custom_width, custom_height))
print(imgResize.shape)
cv2.imshow("The Road Pict RESIZED", imgResize)

# CROP / CUT PICTURE / IMAGE
# crop / cutting part of the width and height of a picture to whatever size we like
# like in self driving car to detect "Lanes", car does not need to process the whole image, just need to see "the road"
# define the starting value of X and Y coordinate, also define the ending value of X and Y coordinate
# in this example img2 have height Y from 0 to 800 and width X from 0 to 1200
# get just the "middle lane of the road" from the width (since the width are 1200 so the middle picture is around position 600
# get just bottom half of the height (that shows the road only, no need the sky, mountain etc)
# opencv cropping format is in [Y,X] (height, width)
imgCropped = img2[400:800,550:650]
# if we want to make the cropped image back to its original size (enlarge the cropped image)
# img2.shape[1] is referring to THE WIDTH or "THE X axis coordinate"
# img2.shape[0] is referring to THE HEIGHT or "THE Y axis coordinate"
# opencv COORDINATES format is in (X,Y)
imgCroppedResized = cv2.resize(imgCropped, (img2.shape[1], img2.shape[0]))
print(imgCropped.shape)
# show the CROPPED IMAGE at its cropped size
cv2.imshow("The Road Pict CROPPED", imgCropped)
# show the CROPPED IMAGE at the original first image size (enlarged/resized)
# note image WILL LOOK BLURRY FOR SURE
cv2.imshow("The Road Pict CROPPED but resized to original image size", imgCroppedResized)

cv2.waitKey(0)