import cv2
import numpy as np

# CREATE PICTURE
# create black, black and white, color image
# create how to create different shape
# create text on image

# create an empty matrix first!
# image with size shape of 500 x 500 means a matrix with 500 x 500 number values
# create blank image with size of 512 x 512, 1 color channel (black or white or intensity of Grayscale)
img0 = np.zeros((512, 512))
# numpy array is by default have all value in FLOATING / DECIMAL value
print(img0)

# create blank image with size of 512 x 512, 3 color channel (color image)
# np.uint8 means change the "default float data" into "UNSIGNED / NON NEGATIVE INTEGER"
img = np.zeros((512, 512,3), np.uint8)

# color by default is BGR (not RGB): Blue, Green, Red
# change color to BLUE
# img[:] means from all Y (height) and all X (width) will be colored as BLUE
#img[:] = 255, 0, 0

# img[0:256,0:256] means from all Y (height) and all X (width) only 25% of TOP PART will be colored as BLUE
img[0:256, 0:256] = 255, 0, 0

# print should show (512, 512, 3)
print(img.shape)

cv2.imshow("my first 25% blue and blank picture", img)
cv2.waitKey(0)

# CREATE A LINE
# make the empty BLACK image size of 512 x 512 with 3 color channels (by default color is black)
img2 = np.zeros((512, 512,3), np.uint8)
# draw a GREEN line (BGR color format of (0,255,0))
# the GREEN line is stretching from coordinates (X,Y) of 0,0 all the way to 300,100
# line thickness is "3"
cv2.line(img2,(0,0),(300,100),(0,255,0),3)

# draw another RED line (BGR color format of (0,0,255))
# the RED line is stretching from coordinates (X,Y) of 0,0 all the way to max X and max Y
# line thickness is "7" (more thicker line)
cv2.line(img2,(0,0),(img.shape[1],img.shape[0]),(0,0,255),7)

cv2.imshow("my line", img2)
cv2.waitKey(0)

# CREATE A RECTANGLE
# create blank image with size of 512 x 512, 3 color channel (color image)
# np.uint8 means change the "default float data" into "UNSIGNED / NON NEGATIVE INTEGER"
imgRect = np.zeros((512, 512,3), np.uint8)
# draw a RED rectangle (BGR color format of (0,0,255))
# the RED rectangle is stretching from :
# coordinates (X,Y) of 350,100 as the "TOP LEFT" coordinate of the rectangle
# coordinated (X,Y) of 450,200 as the "BOTTOM RIGHT" coordinate of the rectangle
# rectangle rectangle line thickness is "2"
cv2.rectangle(imgRect,(350, 100),(450,200), (0, 0, 255),2)

# change rectangle line thickness size so the whole rectangle is filled in with RED color
cv2.rectangle(imgRect,(350, 100),(450,200), (0, 0, 255),cv2.FILLED)

cv2.imshow("my rectangle", imgRect)
cv2.waitKey(0)


# CREATE A CIRCLE
# create blank image with size of 512 x 512, 3 color channel (color image)
# np.uint8 means change the "default float data" into "UNSIGNED / NON NEGATIVE INTEGER"
imgCircle = np.zeros((512, 512,3), np.uint8)
# draw a BLUE circle (BGR color format of (255,0,0))
# the BLUE circle is made from point (X,Y) of 150, 400 with radius of 70
# the BLUE circle line thickness is "10" (more thicker)
cv2.circle(imgCircle,(150, 400), 70, (255, 0, 0),10)

# change circle line thickness size so the whole circle is filled in with RED color
# notice that the circle still have BLUE border line with thickness of "10"
# as the result of the previous command
cv2.circle(imgCircle,(150,400), 70, (0, 0, 255), cv2.FILLED)

cv2.imshow("my circle", imgCircle)
cv2.waitKey(0)

# WRITE A TEXT AT IMAGE
# create blank image with size of width 1200 x height 700, 3 color channel (color image)
# format of opencv SHAPE is always (Y , X , number of color channel)
# np.uint8 means change the "default float data" into "UNSIGNED / NON NEGATIVE INTEGER"
imgWithTxt = np.zeros((700, 1200, 3), np.uint8)
# draw a BLUE circle (BGR color format of (255,0,0))
# the BLUE circle is made from point (X,Y) of 600, 350 with radius of 260
# the BLUE circle line thickness is "40" (more thicker)
cv2.circle(imgWithTxt,(600, 350), 260, (255, 0, 0), 40)

# change circle line thickness size so the whole circle is filled in with GREEN color
# notice that the circle still have BLUE border line with thickness of "40"
# as the result of the previous command
cv2.circle(imgWithTxt,(600, 350), 260, (0, 255, 0), cv2.FILLED)

# write THE TEXT
# text will be put in (X,Y) position of 320,50
# text have font type: HERSHEY COMPLEX
# text have 1.5x font scaling
# text have RED color (0, 0, 255)
# text have thickness of "3"
cv2.putText(imgWithTxt,"Tutorial Draw A SHAPE", (320,50), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 255), 3)

cv2.imshow("my circle", imgWithTxt)
cv2.waitKey(0)