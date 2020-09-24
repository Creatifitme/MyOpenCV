import cv2
import numpy as np
import os

# AUTO CREATE IMAGE CLASSIFIER BASED ON NUMBER OF JPG FILE GIVEN
path = "ImageQuery"

# IMPORT / READ THE IMAGES
images = []
classNames  = []
myList = os.listdir(path)
print("Total Class Detected = ", len(myList))
print("Total Class Detected = ", myList)

orb = cv2.ORB_create(nfeatures = 3000)

for cl in myList:
    # read all files in the directory and import as grayscale
    imgCur = cv2.imread(f'{path}/{cl}',0)
    images.append(imgCur)
    # remove file extension from all the file names in the cl variable
    classNames.append(os.path.splitext(cl)[0])

print(images)
print(classNames)

# find the descriptors of all our "database images"
# store the decriptors in a new list
def findDes(images):
    desList = []
    for imgX in images:
        kp, des = orb.detectAndCompute(imgX,None)
        desList.append(des)

    return desList


# function to check if matching with database file 1 then result is 1
# if matching with database file 2 then result is 2
# etc...
def findID(img, desList, threshold = 15):
    matchedList = []
    # -1 means if no value is match with the image in the database
    finalVal = -1
    # Get the descriptor from the trained image (image that we got from the webcam video)
    kp2, des2 = orb.detectAndCompute(img, None)
    # match descimg with descimgTrain to see how many similarity the 2 descriptors values
    # The common matcher is the brute force matcher
    # k = 2 means there is 2 values that we want to compare
    bf = cv2.BFMatcher()
    try:
        for desX in desList:
            matches = bf.knnMatch(desX, des2, k = 2)
            # decide which is a good match
            # based on the distance of 2 desc
            good = []
            for m, n in matches:
                # find if m is having similar value with n then it is a close match!
                if m.distance < 0.75*n.distance:
                    good.append([m])

            # find the bigger value based on (len(good))
            # the biggest value is the closest match image from the database with the image from the webcam / video
            matchedList.append(len(good))
    except:
        pass
    # print(matchedList)
    if len(matchedList) != 0:
        # define the threshold number so image can be counted match or not
        if max(matchedList) > threshold:
            finalVal = matchedList.index(max(matchedList))
    return finalVal

desList = findDes(images)

# activate webcam to see the real moving object to be matched with the image database
cap = cv2.VideoCapture(0)
while True:
    success, img2 = cap.read()
    # copy img2 to new variable called imgOriginal
    imgOriginal = img2.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    id = findID(img2, desList)

    if id != -1:
        cv2.putText(imgOriginal,classNames[id],(50,50),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)

    cv2.imgshow("IMAGE TO BE TRAIN / DETECTED", imgOriginal)
    cv2.waitKey(1)


# # see how many good matches the software got
# # if the number is big then it is a good match (the img and the imgTrain)
# print(len(good))
#
# img3 = cv2.drawMatchesKnn(img, kpimg, imgTrain, kpimgTrain, good, None, flags=2)
#
# imgKpOri = cv2.drawKeypoints(img, kpimg, None)
# imgKpTrain = cv2.drawKeypoints(imgTrain, kpimgTrain, None)
#
# # show the Keypoints that the orb algorithm found to be useful for matching process
# # cv2.imshow("imgKpOri", imgKpOri)
# # cv2.imshow("imgKpTrain", imgKpTrain)
#
# cv2.imshow("Image Original", img)
# cv2.imshow("Image Training", imgTrain)
# cv2.imshow("Image matched", img3)
#
# cv2.waitKey(0)
#
#


