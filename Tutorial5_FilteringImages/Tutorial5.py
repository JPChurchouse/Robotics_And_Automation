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
    
    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv.filter2D(img, -1, kernel)
    blur = cv.blur(img, (5, 5))
    gaussian = cv.GaussianBlur(img, (5, 5), 0)
    median = cv.medianBlur(img, 5, 0)

    print(f"kernel: {kernel}")

    cv.imshow("img",img)
    cv.imshow("dst",dst)
    cv.imshow("blur",blur)
    cv.imshow("gaussian",gaussian)
    cv.imshow("median",median)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return 0

if __name__ == "__main__":
    sys.exit(main())