import cv2

# open cv offer many tracking: mosse tracker, boosting, csrt, medium flow etc
# mosse tracker has faster speed (higher frame rate) but more bad accuracy
#tracker = cv2.TrackerMOSSE_create()

# mosse tracker has lower speed (lower frame rate) but more better accuracy
# tracker = cv2.TrackerCSRT_create()

############### Tracker Types #####################

# tracker = cv2.TrackerBoosting_create()
# tracker = cv2.TrackerMIL_create()
# tracker = cv2.TrackerKCF_create()
# tracker = cv2.TrackerTLD_create()
tracker = cv2.TrackerMedianFlow_create()
# tracker = cv2.TrackerCSRT_create()
# tracker = cv2.TrackerMOSSE_create()

########################################################

cap = cv2.VideoCapture(1)

# TRACKER INITIALIZATION
# take the first image/video and track it
success, frame = cap.read()

# Make sure "EXTERNAL web camera" is LOADING PERFECTLY
# Without the code (at while True) below,
# some "EXTERNAL webcam" brands will only showing ORANGE SCREEN!
while True:
    success, frame = cap.read()
    cv2.imshow("Temp", frame)
    cv2.destroyWindow("Temp")
    break



# create a bounding box around an image
# bbox is a TUPLE that will have 4 FLOATING values (the X, the Y, the Width, the Height)
bbox = cv2.selectROI("Tracking",frame,False)
# create tracker using the bounding box
tracker.init(frame, bbox)

def drawBox(img,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x,y),((x+w),(y+h)), (255,0,255), 3, 3)
    cv2.putText(img, "Track...", (100, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0),2)

# pressing enter at the "Tracking" output window will start the while loop below
while True:
    timer = cv2.getTickCount()
    success, img = cap.read()

    # this way it will get the bounding box and redraw it all the time
    # until the object is out of the window (LOST)
    success, bbox = tracker.update(img)
    # print(bbox)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "LOST!!!", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)

    cv2.rectangle(img, (15, 15), (200, 90), (255, 0, 255), 2)
    cv2.putText(img, "Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2);
    cv2.putText(img, "Status:", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2);

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    if fps > 60:
        myColor = (20, 230, 20)
    elif fps > 20:
        myColor = (230, 20, 20)
    else:
        myColor = (20, 20, 230)
    cv2.putText(img, str(int(fps)), (75,40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor,2)

    cv2.imshow("Tracking", img)

    # Press "q" at keyboard to exit the video streaming
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# close all video windows that alread opened
cap.release()
cv2.destroyAllWindows()