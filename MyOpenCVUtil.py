import cv2
import numpy as np
import os

# make custom function stackImages to process several images into 1 same window
# the 1 window can be stacked horizontally or vertically
# the window will contain all images that already sized according to the original image size
# parameter 1 (Scale): the scale from the original image
#               1 =  actual scale, <1 = smaller scale, >1 = bigger scale
# parameter 2 (imgArray): all the images that want to be stacked together in 1 window display

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                        imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range (0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale,
                                    scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


# function to get contour of an image and excluding/erasing the noise
# parameter 1 (imgWithEdgeDetected): image that already have edge detected
# parameter 2 (imgOriginal): original image
# parameter 3 (areaToCheck): value of the noise image/noise object to be removed
#               the bigger the value then more image/noise will be remove out
#               more less image/object will be detected!
def getContours(imgWithEdgeDetected, imgOriginal, areaToCheck):
    contours, hierarchy = cv2.findContours(imgWithEdgeDetected, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Draw the contour dot per dot.
    for cnt in contours:
        area = cv2.contourArea(cnt)

        # excluding / erasing the noise out of the contour that we want
        # only draw the contour at the original img (without the noise)
        if area > areaToCheck:
            cv2.drawContours(imgOriginal, cnt, -1, (255, 0, 255), 7)
            # find the actual CORNER POINT of the contour
            # first find the length of the contour
            # True means the contour is CLOSED contour
            # (it is a closed area like a circle or rectangle or square etc)
            peri = cv2.arcLength(cnt, True)
            # approximate what type of SHAPE the contour is (circle or rectangle or square etc)
            # True means the contour is CLOSED contour
            # (it is a closed area like a circle or rectangle or square etc
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            # if the print len result is "4" then the contour is probably shaped as rectangle or square
            # if the print len result is "3" then the contour is probably shaped as triangle
            print(len(approx))

            approxForm = len(approx)

            # Make a GREEN Rectangle Box (color BGR code (0,255,0)) to show the object detected
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgOriginal, (x, y), (x+w, y+h), (0,255,0), 5)
            # display the number of image point detected (is it a possible rectangle or triangle etc)
            cv2.putText(imgOriginal, "Point: " + str(len(approx)),
                        (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0,255,0),2)
            # change the area value to integer so the text display is easier to read
            cv2.putText(imgOriginal, "Area: " + str(int(area)),
                        (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)


