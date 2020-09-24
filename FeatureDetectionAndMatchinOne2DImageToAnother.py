import cv2
import numpy as np

path = "ImageQuery/KinectSportSeasonTwo.jpg"
pathTrain = "ImageTrain/KinectSportSeasonTwoTRAIN.jpg"

# read all images to be compared as GRAYSCALE (the "0" parameter value)
# this is to make the comparison more easier
# IMPORT / READ THE IMAGES!
img = cv2.imread(path,0)
imgTrain = cv2.imread(pathTrain,0)


# Create the image detector (descriptive) so can easily identify image
# using orb algorithm, the free to use one and fast one
# nfeatures parameter means increase the number of features the orb has to find
# nfeatures default value is 500
orb = cv2.ORB_create(nfeatures = 3000)

# find the key points and the decriptor for img and imgTrain
kpimg, descimg = orb.detectAndCompute(img, None)
kpimgTrain, descimgTrain = orb.detectAndCompute(imgTrain, None)

# match descimg with descimgTrain to see how many similarity the 2 descriptors values
# the common matcher is the brute force matcher
# k = 2 means there is 2 values that we want to compare
bf = cv2.BFMatcher()
matches = bf.knnMatch(descimg, descimgTrain, k = 2)

# decide which is a good match
# based on the distance of 2 desc
good = []
for m, n in matches:
    # find if m is having similar value with n then it is a close match!
    if m.distance < 0.75*n.distance:
        good.append([m])

# see how many good matches the software got
# if the number is big then it is a good match (the img and the imgTrain)
print(len(good))

img3 = cv2.drawMatchesKnn(img, kpimg, imgTrain, kpimgTrain, good, None, flags=2)

imgKpOri = cv2.drawKeypoints(img, kpimg, None)
imgKpTrain = cv2.drawKeypoints(imgTrain, kpimgTrain, None)

# show the Keypoints that the orb algorithm found to be useful for matching process
# cv2.imshow("imgKpOri", imgKpOri)
# cv2.imshow("imgKpTrain", imgKpTrain)

cv2.imshow("Image Original", img)
cv2.imshow("Image Training", imgTrain)
cv2.imshow("Image matched", img3)

cv2.waitKey(0)



