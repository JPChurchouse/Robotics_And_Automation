import os
import sys

import cv2 as cv
import numpy as np

def main():
    filepath = os.getcwd() + "/Tutorial3/frame.png"

    img_1 = np.zeros((480, 640, 1), dtype=np.uint8)
    img_2 = np.zeros((480, 640, 1), dtype=np.uint8)
    
    cv.rectangle(img_1, (300, 220), (600, 440), (255), -1)
    cv.rectangle(img_2, (40, 40), (360, 260), (255), -1)
    
    img_add = cv.add(img_1, img_2)
    img_sub = cv.subtract(img_1, img_2)
    
    cv.imshow("img_1", img_1)
    cv.imshow("img_2", img_2)
    cv.imshow("img_add", img_add)
    cv.imshow("img_sub", img_sub)
    
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())