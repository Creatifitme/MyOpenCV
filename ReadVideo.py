import cv2

# READ A VIDEO FILE OR STREAMING VIDEO FROM AVAILABLE COMPUTER WEBCAM
frameWidth = 1024
frameHeight = 720

# These 2 code lines can be replaced with:
# img = cv2.resize(img,(frameWidth, frameHight)) put inside the While True loop
# the cv2.resize put inside while true loop have advantage: can be "Custom width" x "Custom height" size...
# Disadvantage of these 2 code lines is the frameWidht and frameHeight must be
# in predefined standard like 640 x 480 or 1280 x 720 or 1920 x 1080
# CAN NOT be "Custom width" x "Custom height" size...
#cap.set(3, frameWidth)
#cap.set(4, frameHeight)

# cv2.VideoCapture(0) means capture from a "default web camera"
# (1 means capture from second web camera etc)
capture = cv2.VideoCapture(0)
# cv2.VideoCapture("video file name") means capture/play a video file
#capture = cv2.VideoCapture("Resources/testVideo.mp4")
while True:
    success, img = capture.read()
# resize the video image as custom frame size (as we like)
    img = cv2.resize(img,(frameWidth, frameHeight))
# create a new window named "MyVideo"
    cv2.imshow("MyVideo", img)
# Press "q" at keyboard to exit the video streaming
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#close all video windows that alread opened
capture.release()
cv2.destroyAllWindows()