import cv2
import numpy as np

# WARP PERSPECTIVE / BIRD or TOP VIEW OF AN IMAGE
path = "Resources/cards.jpg"
img = cv2.imread(path)

# we need to know all the 4 points coordinate (top left, top right, bottom left, bottom right)
# to be able to convert any image into 2D image
# find out the 4 coordinates by opening MSPAINT, enlarge the image there and hover the mouse cursor to all 4 points mentioned at the image
# write down the value in a paper and put the value in code below
# coordinate system at MSPAINT and opencv is same = X,Y
# we get first point (top left) coordinate X,Y = 111,219
# we get second point (top right) coordinate X,Y = 287,188
# we get third point (bottom left) coordinate X,Y = 154,482
# we get fourth point (bottom right) coordinate X,Y = 352,440
points = np.float32([[111,219],[287,188],[154,482],[352,440]])

# create a RED circle/ RED DOT (BGR code of (0,0,255)) with radius of 5
# to check the 4 points position
# is first point at the top left (as it should)
# is second point at the top right (as it should)
# is third point at the bottom left (as it should)
# is fourth point at the bottom right (as it should)
for x in range(0,4):
    cv2.circle(img,(points[x][0], points[x][1]), 5, (0,0,255),cv2.FILLED)

cv2.imshow("Original Image", img)

# create the new image view for new warp / bird view width and height
width = 250
height = 350
# create "new points coordinate" to create the "warp / bird view" from the original random positioned image
# define:
# THE NEW first point (top left) coordinate X,Y = 0,0
# THE NEW second point (top right) coordinate X,Y = width,0
# THE NEW third point (bottom left) coordinate X,Y = 0,height
# THE NEW fourth point (bottom right) coordinate X,Y = width,height
pointsWarp = np.float32([[0,0],[width,0],[0,height],[width,height]])
# transform the image we wanted from unclear random original image position
# into the X,Y position we wanted (WARP / Bird view position that we wanted)
matrix = cv2.getPerspectiveTransform(points, pointsWarp)
imgOutput = cv2.warpPerspective(img, matrix,(width, height))
cv2.imshow("Warped / Bird View Image", imgOutput)

cv2.waitKey(0)