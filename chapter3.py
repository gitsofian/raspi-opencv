import cv2
import numpy as np

img = cv2.imread("res/img-fhd-1.jpg")

cv2.imshow("Image", img)

cv2.waitKey(0)
