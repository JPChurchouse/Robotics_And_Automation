import os
import sys

import cv2 as cv
import numpy as np

def main():

    filepath = os.getcwd() + "/apples.png"
    img = cv.imread(filepath, cv.IMREAD_COLOR)

    if (img is None):
        print(f'Error: Image not found')
        return 1

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    redLower = cv.inRange(hsv, (0, 0, 0), (15, 255, 255))
    redUpper = cv.inRange(hsv, (165, 0, 0), (180, 255, 255))
    red = cv.add(redLower, redUpper)

    green = cv.inRange(hsv, (22, 0, 0), (62, 255, 255))

    blue = cv.inRange(hsv, (64, 0, 0), (104, 255, 255))

    cv.imshow("img", img)
    cv.imshow("hsv", hsv)
    cv.imshow("red", red)
    cv.imshow("green", green)
    cv.imshow("blue", blue)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return 0

if __name__ == "__main__":
    sys.exit(main())