import cv2
import numpy as np
from utils.remove_noise import remove_noise

lower = np.array([0, 0, 20])
upper = np.array([30, 140, 80])
def findContours(img,min_area=5):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    bg_mask = cv2.inRange(hsv, lower, upper)
    box_mask = cv2.bitwise_not(bg_mask)
    box_mask = remove_noise(box_mask, min_area)
    contours, _ = cv2.findContours(box_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours
