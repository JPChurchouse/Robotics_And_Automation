import os
import sys

import cv2 as cv
import numpy as np

def main():

    img = np.zeros((480, 640, 1), dtype=np.uint8)

    window = cv.namedWindow("img")
    cv.imshow("img", img)
    cv.waitKey(0)
    cv.destroyWindow("img")
    return 0

if __name__ == "__main__":
    sys.exit(main())