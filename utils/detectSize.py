import cv2
def detectSize(contour,cm_per_px):

    x, y, w, h = cv2.boundingRect(contour)

    area = cv2.contourArea(contour)
    w_cm = w * cm_per_px
    h_cm = h * cm_per_px

    print(f"Ширина: {w_cm:.2f} см")
    print(f"Длина: {h_cm:.2f} см")
    print(f"Ширина: {w}px")
    print(f"Длина: {h}px")
    print(f"Площадь (по контуру): {area}px^2")
    print(f"Площадь (прямоугольник): {w * h}px^2")