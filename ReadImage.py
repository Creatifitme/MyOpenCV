import cv2
import numpy as np

# READ AND MANIPULATE STILL IMAGE PICTURE

# make a 5 x 5 matrix that have all "1" values, set the value as integer (not float)
# do not forget to import numpy first
kernel = np.ones((5,5),np.uint8)
# print the 5 x 5 matrix that shows all value item inside it is "1"
#print(kernel)

path = "Resources/lena.png"

# cv2.imread(path,0) =  "0" means make the picture to GRAYSCALE (not color)
img = cv2.imread(path)

# FIVE "MUST KNOWN OPENCV FUNCTIONS":
# 1. Convert picture to grayscale
# 2. Convert picture to be more blurry
# 3. Convert picture to have EDGE DETECTED (into black and have some edge detected in white lines)
# 4. Convert picture with EDGE DETECTED to be DILATION (increase/thicking the white lines)
# 5. Convert picture with EDGE DETECTED to be EROSION (decrease/thinning the white lines)

# make new variable to convert color image to grayscale image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# make new variable to convert grayscale image to color image
#imgColor = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

# make image blurry (the (x,y) parameter must always be an ODD number, more higher number= more blurry)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)

# make an EDGE DETECTOR (important as the detector of an image, the (x,y) parameter
# if more smaller value then more detail EDGE (more EDGE) will be detected)
imgCanny = cv2.Canny(imgBlur,100,200)

# make image that already EDGE DETECTED, the LINE size can be increased (DILATION) - more thicker line
# iterations parameter value :
# the bigger the value then the THICKER the line will be at the edge detected picture
imgDilation = cv2.dilate(imgCanny,kernel, iterations=2)

# make image that already EDGE DETECTED, the LINE size can be decreased (EROSION) - more thinner line
# iterations parameter value :
# the bigger the value then the THINNER the line will be at the edge detected picture
imgEroded = cv2.erode(imgDilation,kernel, iterations=1)

#create a new window named "Lena" to show the picture
cv2.imshow("Lena", img)
cv2.imshow("LenaGray", imgGray)
cv2.imshow("LenaGrayBlur", imgBlur)
cv2.imshow("LenaGrayBlurEDGE", imgCanny)
cv2.imshow("LenaDILATION", imgDilation)
cv2.imshow("LenaERODED", imgEroded)
cv2.waitKey(0)



