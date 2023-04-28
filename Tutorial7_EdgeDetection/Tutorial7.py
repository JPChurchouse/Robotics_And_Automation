import os
import sys

import cv2 as cv
import numpy as np

def main():

    filepath = os.getcwd() + "/apples.png"
    img = cv.imread(filepath, cv.IMREAD_COLOR)

    if (img is None):
        print(f'Error:Image not found')
        return 1

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    canny = cv.Canny(gray, 127, 255)
    cv.imshow("img", img)

    cv.imshow("gray", gray)

    cv.imshow("canny", canny)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return 0

if __name__ == "__main__":
    sys.exit(main())