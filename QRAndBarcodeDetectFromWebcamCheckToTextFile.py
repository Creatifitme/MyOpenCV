import cv2
import numpy as np
from pyzbar.pyzbar import decode

# DETECTING MANY BARCODE AND QRCODE FROM A WEBCAM
frameWidth = 640
frameHeight = 480
#img = cv2.imread("Resources/employeeBarcode.png")
cap = cv2.VideoCapture(0)

with open("MyDataFile.txt") as f:
    # read all the text file and based on new line will add new 1 item to the list
    myDataList = f.read().splitlines()


while True:
    success, img = cap.read()
    # resize the video image as custom frame size (as we like)
    img = cv2.resize(img, (frameWidth, frameHeight))
# the "code" variable will contains:
# the data, which type (qr or barcode)
# the bounding box location
# the polygon points
    for individual_barcode in decode(img):
        # convert the DATA part into strings
        myData = individual_barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            print("Authorized Person")
            myOutput = "Authorized Person"
            myColor = (0,255,0)
        else:
            print("Un-Authorized Person")
            myOutput = "Un-Authorized Person"
            myColor = (0, 0, 255)
        # print a bounding box around the detected qr/barcode
        pts = np.array([individual_barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        # True means the polygon is CLOSED form
        cv2.polylines(img,[pts],True,myColor,5)
        # make sure the text written still readable, not following the polygon
        # text following the rectangle pattern and always on top of the rectangle
        topPoint = individual_barcode.rect
        cv2.putText(img,myOutput,(topPoint[0],topPoint[1]),cv2.FONT_HERSHEY_SIMPLEX,1,myColor,2)

# create a new window named "MyVideo"
    cv2.imshow("MyVideo", img)
# Press "q" at keyboard to exit the video streaming
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break