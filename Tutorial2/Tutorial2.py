import os
import sys

import cv2 as cv
import numpy as np

def main():
    filepath = os.getcwd() + "/Tutorial2/frame.png"

    camera = cv.VideoCapture(0)

    if (not camera.isOpened()):
        print(f"ERR: not found")
        return 1
    
    ret, frame = camera.read()

    if (frame is None):
        print(f"ERR - no image")
        return 2

    cv.imwrite(filepath, frame)
    cv.imshow("frame", frame)
    cv.waitKey(0)
    cv.destroyWindow("frame")
    return 0

if __name__ == "__main__":
    sys.exit(main())