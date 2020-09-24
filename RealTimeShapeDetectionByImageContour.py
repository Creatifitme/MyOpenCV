import cv2
import numpy as np
import MyOpenCVUtil as MyCV

# create empty functions that do nothing, just to satisfied the cv2.trackbar parameter
def empty(x):
    pass

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold 1","Parameters",23,255,empty)
cv2.createTrackbar("Threshold 2","Parameters",20,255,empty)
# Create bounding area to detect real object (and eliminate noise object)
# minimum value 5000 and max value to detect is 30000
cv2.createTrackbar("Area","Parameters",5000,30000,empty)

while True:
    _, img = cap.read()
    # copy the img variable image/video content to new variable named imgContour
    imgContour = img.copy()

    img = cv2.resize(img, (frameWidth, frameHeight))

    # make image blurry (the (x,y) parameter must always be an ODD number,
    # more higher number= more blurry)
    imgBlur = cv2.GaussianBlur(img, (7,7),1)

    # make new variable to convert color image to grayscale image
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold 1","Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold 2","Parameters")
    areaMin = cv2.getTrackbarPos("Area", "Parameters")

    # make an EDGE DETECTOR (important as the detector of an image, the (x,y) parameter
    # if more smaller value then more detail EDGE (more EDGE) will be detected)
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

    # create kernel to make image DILATION (to remove the noise in image)
    kernel = np.ones((5, 5), np.uint8)
    # make image that already EDGE DETECTED, the LINE size can be increased (DILATION) - more thicker line
    # iterations parameter value :
    # the bigger the value then the THICKER the line will be at the edge detected
    imgDilate = cv2.dilate(imgCanny,kernel,iterations=1)

    MyCV.getContours(imgDilate, imgContour, areaMin)

    imgStack = MyCV.stackImages(0.8, ([img, imgGray, imgCanny],
                                      [imgDilate, imgContour, imgDilate]))
    cv2.imshow("Result", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break