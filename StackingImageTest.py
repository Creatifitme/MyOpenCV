import cv2
import numpy as np

# JOINING SEVERAL IMAGES INTO 1 IMAGE WINDOW
# make custom function stackImages to process several images into 1 window
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



# make a 5 x 5 matrix that have all "1" values, set the value as integer (not float)
# do not forget to import numpy first
kernel = np.ones((5,5),np.uint8)

path = "Resources/lena.png"
# READ AND MANIPULATE STILL IMAGE PICTURE
# cv2.imread(path,0) =  "0" means make the picture to GRAYSCALE (not color)
img = cv2.imread(path)

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
# Picture will be SCALED DOWN 0.8 (80%) from original size
#finalStackedImages = stackImages(0.8, ([img, imgGray, imgBlur],[imgCanny, imgEroded, imgDilation]))

# stack all images together and fill in some empty spaces with blank black images as stated in the imgBlank
# the function stackImages automatically make all image into same size with original image size
imgBlank = np.zeros((200,200), np.uint8)

# create a stacked image with matrix image size of 4 columns and 2 rows
# Picture will be SCALED DOWN 0.6 (60%) from original size
finalStackedImages = stackImages(0.6, ([img, imgGray, imgBlur, imgDilation],[imgCanny, imgBlank, imgEroded, imgBlank]))

cv2.imshow("Final Stacked Images", finalStackedImages)
#create a new window named "Lena" to show the picture
#cv2.imshow("Lena", img)
#cv2.imshow("LenaGray", imgGray)
#cv2.imshow("LenaGrayBlur", imgBlur)
#cv2.imshow("LenaGrayBlurEDGE", imgCanny)
#cv2.imshow("LenaDILATION", imgDilation)
#cv2.imshow("LenaERODED", imgEroded)
cv2.waitKey(0)

