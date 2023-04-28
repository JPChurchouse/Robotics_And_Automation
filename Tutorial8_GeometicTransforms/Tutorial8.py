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

    print(img.shape)
    resized = cv.resize(img, None, fx=0.5, fy=0.5)

    T = np.array([[1, 0, 160],[0, 1, 120]], dtype=np.float32)
    translated = cv.warpAffine(img, T, (640, 360))
    
    R = cv.getRotationMatrix2D((320, 180),90,1)
    rotated = cv.warpAffine(img, R, (640, 360))

    pts1 = np.array([[50, 50], [200, 50], [50, 200]], dtype=np.float32)
    pts2 = np.array([[10,100],[200,50],[100,250]], dtype=np.float32)
    A = cv.getAffineTransform(pts1, pts2)
    warped_A = cv.warpAffine(img, A, (640, 360))

    pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    P = cv.getPerspectiveTransform(pts1,pts2)
    warped_P = cv.warpPerspective(img, P, (640,360))

    cv.imshow("img", img)
    cv.imshow("resized", resized)
    cv.imshow("translated", translated)
    cv.imshow("rotated", rotated)
    cv.imshow("warped_A", warped_A)
    cv.imshow("warped_P", warped_P)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return 0

if __name__ == "__main__":
    sys.exit(main())