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

    contours, hierarchy = cv.findContours(red, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    print(f"Contours detected: {len(contours)}")

    draw = cv.copyTo(img, None)
    for c in contours:
        cv.drawContours(draw, [c], 0, (0, 0, 255), 3)

    cv.imshow("img", img)
    cv.imshow("red", red)
    cv.imshow("draw", draw)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return 0

if __name__ == "__main__":
    sys.exit(main())