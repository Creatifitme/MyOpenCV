import cv2

# threshold to detect object
thresVar = 0.5


# READ A VIDEO FILE OR STREAMING VIDEO FROM AVAILABLE COMPUTER WEBCAM
frameWidth = 1024
frameHeight = 720

#img = cv2.imread('lena.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


# fill in all data in coco.names file into the classNames list automatically
# by detecting the enter (\n) character
classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
print(classNames)

# import configuration files ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt
# the ssd_mobilenet is better then YOLO in term of speed of detection
# and can be run only by using standard laptop (without special VGA card)
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

# create the Model to Detect Objects
# model will give ID-number of the object detected
# we just need to map it to the classNames above to find the "object name"
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# cv2.VideoCapture(0) means capture from a "default web camera"
# (1 means capture from second web camera etc)
cap_array = []
maxCam = 3
for i in range(0, maxCam):
    capture= cv2.VideoCapture(i)
    if not capture.isOpened():
        print
        "error opening ", i
    else:
        cap_array.append(capture)

img = []
m = 0
while True:
    for k in range(0, maxCam):
        success, img = cap_array[k].read()
        # resize the video image as custom frame size (as we like)
        img = cv2.resize(img, (frameWidth, frameHeight))

        # Press "q" at keyboard to exit the video streaming

        # detect object if more then 50% (0.5) then it is considered as object
        # otherwise just ignore it
        classIds, confs, bbox = net.detect(img, confThreshold=thresVar)
        print(classIds, bbox)

        # Check the camera MUST DETECT SOMETHING FIRST, not just empty view
        if len(classIds) != 0:
            # Make just 1 for loop to do 3 variable loooing at once (use zip function)
            for classIdVar, confidenceVar, boxVar in zip(classIds.flatten(), confs.flatten(), bbox):
                cv2.rectangle(img, boxVar, color=(0,255,0),thickness=3)
                cv2.putText(img, classNames[classIdVar-1].upper(),(boxVar[0]+10,boxVar[1]+30)
                            ,cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                cv2.putText(img, str(round(confidenceVar*100,2)).join(' %'), (boxVar[0] + 200, boxVar[1] + 30)
                            , cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        # create a new window named "MyVideo"
        cv2.imshow("MyVideo " + str(k + 1), img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# close all video windows that already opened
capture.release()
cv2.destroyAllWindows()