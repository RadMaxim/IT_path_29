import cv2
def resizeShape(img,size=2):

    shape = img.shape
    return cv2.resize(img, (shape[1] // size, shape[0] // size))