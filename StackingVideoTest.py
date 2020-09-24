import cv2
import MyOpenCVUtil as MyCV
import numpy as np

# JOINING SEVERAL VIDEO FROM WEBCAM INTO 1 VIDEO WINDOW

# READ A VIDEO FILE OR STREAMING VIDEO FROM AVAILABLE COMPUTER WEBCAM
frameWidth = 640
frameHight = 480

# cv2.VideoCapture(0) means capture from a "default web camera" (1 means capture from second web camera etc)
#capture = cv2.VideoCapture(0)
# cv2.VideoCapture("video file name") means capture/play a video file
capture = cv2.VideoCapture(0)
while True:
    success, img = capture.read()
# resize the video image as custom frame size (as we like)
    img = cv2.resize(img,(frameWidth, frameHight))
# create a new window named "MyVideo"
    #cv2.imshow("MyVideo", img)

    kernel = np.ones((5,5),np.uint8)

    # make new variable to convert color image to grayscale image
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # make image blurry (the (x,y) parameter must always be an ODD number, more higher number= more blurry)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)

    # make an EDGE DETECTOR (important as the detector of an image, the (x,y) parameter if more smaller value then more detail EDGE (more EDGE) will be detected)
    imgCanny = cv2.Canny(imgBlur,100,200)

    # make image that already EDGE DETECTED, the LINE size can be increased (DILATION) - more thicker line
    # iterations parameter value : the bigger the value then the THICKER the line will be at the edge detected picture
    imgDilation = cv2.dilate(imgCanny,kernel, iterations=2)

    # make image that already EDGE DETECTED, the LINE size can be decreased (EROSION) - more thinner line
    # iterations parameter value : the bigger the value then the THINNER the line will be at the edge detected picture
    imgEroded = cv2.erode(imgDilation,kernel, iterations=1)

    # stack all images together, the function stackImages automatically make all image into same size with original image size
    # make a 8 rows x 6 columns of videos stacking
    # Picture will be SCALED DOWN 0.18 (18%) from original size
    finalStackedVideo = MyCV.stackImages(0.18, ([img, imgGray, imgBlur, imgCanny, imgEroded, imgDilation],
                                           [img, imgGray, imgBlur, imgCanny, imgEroded, imgDilation],
                                           [img, imgGray, imgBlur, imgCanny, imgEroded, imgDilation],
                                           [img, imgGray, imgBlur, imgCanny, imgEroded, imgDilation],
                                           [img, imgGray, imgBlur, imgCanny, imgEroded, imgDilation],
                                           [img, imgGray, imgBlur, imgCanny, imgEroded, imgDilation],
                                           [img, imgGray, imgBlur, imgCanny, imgEroded, imgDilation],
                                           [img, imgGray, imgBlur, imgCanny, imgEroded, imgDilation]
                                           ))

    # stack all images together and fill in some empty spaces with blank black images as stated in the imgBlank
    # the function stackImages automatically make all image into same size with original image size
    imgBlank = np.zeros((200,200), np.uint8)

    # create a stacked image with matrix image size of 4 columns and 2 rows
    # Picture will be SCALED DOWN 0.4 (40%) from original size
    #finalStackedVideo= stackImages(0.4, ([img, imgGray, imgBlur, imgDilation],[imgCanny, imgBlank, imgEroded, imgBlank]))

    cv2.imshow("Final Stacked Video", finalStackedVideo)
    #create a new window named "Lena" to show the picture
    #cv2.imshow("Lena", img)
    #cv2.imshow("LenaGray", imgGray)
    #cv2.imshow("LenaGrayBlur", imgBlur)
    #cv2.imshow("LenaGrayBlurEDGE", imgCanny)
    #cv2.imshow("LenaDILATION", imgDilation)
    #cv2.imshow("LenaERODED", imgEroded)
    # Press "q" at keyboard to exit the video streaming
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



