import os
import sys

import cv2 as cv
import numpy as np
import random

def main():

    img = np.zeros((480, 640), dtype=np.uint8)

    for i in range(100):
        x = random.randint(0, 640)
        y = random.randint(0, 480)
        r = random.randint(0, 3)
        cv.circle(img, (x, y), r, 255, -1)

    cv.circle(img, (320, 240), 100, 255, 25)
    cv.circle(img, (320, 240), 150, 255, 25)
    

    kernel = cv.getStructuringElement(cv.MORPH_RECT,(10,10))
    print(f"kernel:\n{kernel}")
    erode = cv.erode(img, kernel, iterations=1)
    dilate = cv.dilate(img, kernel, iterations=1)
    opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
    cv.imshow("img", img)
    cv.imshow("erode", erode)
    cv.imshow("dilate", dilate)
    cv.imshow("opening", opening)
    cv.imshow("closing", closing)
    
    
    cv.waitKey(0)
    cv.destroyAllWindows()

    return 0

if __name__ == "__main__":
    sys.exit(main())