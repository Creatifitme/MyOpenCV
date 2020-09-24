import cv2
import numpy as np

frameWidth = 480
frameHeight = 320

cap = cv2.VideoCapture(1)

# These 2 code lines can be replaced with:
# img = cv2.resize(img,(frameWidth, frameHight)) put inside the While True loop
# the cv2.resize put inside while true loop have advantage: can be "Custom width" x "Custom height" size...
# Disadvantage of these 2 code lines is the frameWidht and frameHeight must be
# in predefined standard like 640 x 480 or 1280 x 720 or 1920 x 1080
# CAN NOT be "Custom width" x "Custom height" size...
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

# create empty functions that do nothing, just to satisfied the cv2.trackbar parameter
def empty(x):
    pass

# Find out the minimum and maximum value for the hue, saturation, value
# create new "TRACKBAR window" to search / play around to get the optimum min and max HUE value
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
# normal hue range is from 0 to 360
# opencv hue range is only from 0 to 179
# opencv saturation range is only from 0 to 255
# opencv value range is only from 0 to 255
# create all 6 "TRACKBAR window"
# to play around for min-max of the hue, saturation, value
cv2.createTrackbar("Hue min","HSV",0,179,empty)
cv2.createTrackbar("Hue max","HSV",179,179,empty)
cv2.createTrackbar("Sat min","HSV",0,255,empty)
cv2.createTrackbar("Sat max","HSV",255,255,empty)
cv2.createTrackbar("Val min","HSV",0,255,empty)
cv2.createTrackbar("Val max","HSV",255,255,empty)

while True:
    # no need to get the status true/false (success/not success) to "_" (ignore it)
    # get the result of cap.read to img variable
    _, img = cap.read()

    img = cv2.resize(img, (frameWidth, frameHeight))
    # convert the standard opencv color channel of BGR (Blue, Green, Red) color space
    # into HSV (easier to convert rather then BGR
    # Hue = the color
    # Saturation = how pure the color is
    # Value = how bright the color is
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # Grab/get the correct optimum value for Hue-Saturation-Value
    h_min = cv2.getTrackbarPos("Hue min","HSV")
    h_max = cv2.getTrackbarPos("Hue max", "HSV")
    s_min = cv2.getTrackbarPos("Sat min", "HSV")
    s_max = cv2.getTrackbarPos("Sat max", "HSV")
    v_min = cv2.getTrackbarPos("Val min", "HSV")
    v_max = cv2.getTrackbarPos("Val max", "HSV")

    # put the ideal/optimal hue-sat-value into a numpy variable
    # set the lower / minimal Hue, Sat, Val
    lower = np.array([h_min, s_min, v_min])
    # set the upper / maximal Hue, Sat, Val
    upper = np.array([h_max, s_max, v_max])
    # create a mask to generate image value just on this optimal range
    # create the mask of the image based on optimal HSV color that we wanted
    imgMyMask = cv2.inRange(imgHSV, lower, upper)

    # output the end result of the image based on the HSV color we wanted
    # using bitwise AND logic as to merge original image + new HSV image
    # whatever exist in the original image AND exist in the new HSV image,
    # then we take that final image
    imgMaskResult = cv2.bitwise_and(img, img, mask= imgMyMask )

    # stack picture together horizontally using hstack or vertically using vstack
    # note that hstack and vstack ONLY WORK if the image is in the same color channel
    # CAN NOT do hstack or vstack for images with "DIFFERENT NUMBER OF COLOR CHANNELS"!
    # (example: can not stacking grayscale with color image)
    # imgHstack = np.hstack([img,imgMaskResult])
    # Convert imgMyMask from graysacle to 3 channels color HSV
    # so it can all be outputted into the same window using hstack or vstack
    img3chnlMsk = cv2.cvtColor(imgMyMask, cv2.COLOR_GRAY2BGR)

    imgHstack = np.hstack([img, img3chnlMsk, imgMaskResult])

    # cv2.imshow("Original", img)
    # cv2.imshow("Image with HSV", imgHSV)
    # cv2.imshow("Image mask that I define", imgMyMask)
    # cv2.imshow("Mask that I wanted", imgMaskResult)
    cv2.imshow("Original and the Mask that I wanted", imgHstack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#close all video windows that alread opened
cap.release()
cv2.destroyAllWindows()