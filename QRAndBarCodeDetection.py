import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread("Resources/employeeBarcode.png")

# decode the barcode within the image
code = decode(img)

# the "code" variable will contains:
# the data, which type (qr or barcode)
# the bounding box location
# the polygon points
for individual_barcode in code:
    # print the data part of the barcode/qr, assuming 1 image contain more then 1 barcode/qr code
    # the data is always in byte (need to decode it again)
    print(individual_barcode.data)
    # print the rect shape of barcode/qr code (left, top, width, height value)
    print(individual_barcode.rect)

    # convert the DATA part into strings
    myData = individual_barcode.data.decode('utf-8')
    print(myData)

