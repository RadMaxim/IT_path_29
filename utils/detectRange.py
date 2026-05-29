import cv2
import numpy as np
def nothing(x):
    pass

cv2.namedWindow("HSV Controls")
cv2.namedWindow("Mask")
cv2.namedWindow("Result")

# Нижний предел HSV
cv2.createTrackbar("H min", "HSV Controls", 0, 179, nothing)
cv2.createTrackbar("S min", "HSV Controls", 0, 255, nothing)
cv2.createTrackbar("V min", "HSV Controls", 0, 255, nothing)

# Верхний предел HSV
cv2.createTrackbar("H max", "HSV Controls", 179, 179, nothing)
cv2.createTrackbar("S max", "HSV Controls", 255, 255, nothing)
cv2.createTrackbar("V max", "HSV Controls", 255, 255, nothing)


def detectRangeBg():
    h_min = cv2.getTrackbarPos("H min", "HSV Controls")
    s_min = cv2.getTrackbarPos("S min", "HSV Controls")
    v_min = cv2.getTrackbarPos("V min", "HSV Controls")

    h_max = cv2.getTrackbarPos("H max", "HSV Controls")
    s_max = cv2.getTrackbarPos("S max", "HSV Controls")
    v_max = cv2.getTrackbarPos("V max", "HSV Controls")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    return {lower:lower,upper:upper}