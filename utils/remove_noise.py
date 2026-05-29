import cv2
import numpy as np

def remove_noise(mask, min_area=5000):
    # убираем одиночные шумы
    kernel_open = np.ones((5, 5), np.uint8)
    cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open)

    # закрываем небольшие дырки внутри объекта
    kernel_close = np.ones((15, 15), np.uint8)
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel_close)

    # оставляем только крупные области
    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    filtered = np.zeros_like(mask)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area >= min_area:
            cv2.drawContours(filtered, [cnt], -1, 255, thickness=cv2.FILLED)

    return filtered