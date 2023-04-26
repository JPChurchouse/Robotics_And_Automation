import os
import sys

import cv2 as cv
import numpy as np

def main():

    filepath = os.getcwd() + "/Tutorial2/apples.png"
    img = cv.imread(filepath, cv.IMREAD_COLOR)

    if (img is None):
        print(f"Error: {filepath} Image not found!!!")
        return 1

    #window = cv.namedWindow("img")
    cv.imshow("img", img)
    cv.waitKey(0)
    cv.destroyWindow("img")
    return 0

if __name__ == "__main__":
    sys.exit(main())