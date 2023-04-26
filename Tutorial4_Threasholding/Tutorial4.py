import os
import sys
import cv2 as cv
import numpy as np


def main():
    filepath = os.getcwd() + "/Tutorial4_Threasholding/gradient.png"
    img = cv.imread(filepath, cv.IMREAD_GRAYSCALE)
    if (img is None):
        print(f'Error:Image not found')
        return 1
    ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    ret, thresh_inv = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
    cv.imshow("img", img)
    cv.imshow("thresh", thresh)
    cv.imshow("thresh_inv", thresh_inv)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return 0


if __name__ == "__main__":
    sys.exit(main())
