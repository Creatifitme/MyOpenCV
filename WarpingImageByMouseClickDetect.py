import cv2
import numpy as np

# create function to detect a mouse click
def mousePoints(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter += 1


# create circles matrix that contain 4 rows and 2 columns to store all 4 points of 2 values: the X, the Y
# the top left, top right, bottom left, bottom right (X,Y)
# first fill it with all ZERO values integer
circles = np.zeros((4,2), np.int)
counter = 0

path = "Resources/book.jpg"
# MAKE WARPING / BIRD VIEW OF AN IMAGE BY DETECTING "LEFT BUTTON MOUSE CLICK"
img = cv2.imread(path)

while True:
    if counter == 4:
        # we need to know all the 4 points coordinate (top left, top right, bottom left, bottom right)
        # to be able to convert any image into 2D image
        # find out the 4 coordinates by opening MSPAINT, enlarge the image there and hover the mouse cursor to all 4 points mentioned at the image
        # write down the value in a paper and put the value in code below
        # coordinate system at MSPAINT and opencv is same = X,Y
        # MUST FOLLOW THE PATTERN BELOW!!
        # first point must be (top left) coordinate X,Y = X,Y value at circles[0]
        # second point must be (top right) coordinate X,Y = X,Y value at circles[1]
        # third point must be (bottom left) coordinate X,Y = X,Y value at circles[2]
        # fourth point must be (bottom right) coordinate X,Y = X,Y value at circles[3]
        points = np.float32([circles[0],circles[1],circles[2],circles[3]])

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

        # wait until the warped image window AND original image window all are closed then BREAK EXIT THIS CODE!!
        cv2.waitKey(0)
        break

    # create a RED circle/ RED DOT (BGR code of (0,0,255)) with radius of 5
    # to check the 4 points position
    # is first point at the top left (as it should)
    # is second point at the top right (as it should)
    # is third point at the bottom left (as it should)
    # is fourth point at the bottom right (as it should)
    for x in range(0,4):
        cv2.circle(img,(circles[x][0], circles[x][1]), 8, (0,0,255),cv2.FILLED)

    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    # wait until all 4 mouse clicks has been registered
    cv2.waitKey(1)
