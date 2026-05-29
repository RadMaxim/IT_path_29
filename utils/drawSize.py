import cv2

def draw_box_size(image, cnt, cm_per_px):
    result = image.copy()

    x, y, w, h = cv2.boundingRect(cnt)
    print(x,y,w,h)
    # перевод в сантиметры
    real_w = w * cm_per_px
    real_h = h * cm_per_px

    # рамка
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # линия ширины (сверху)
    cv2.line(result, (x, y - 20), (x + w, y - 20), (255, 0, 0), 2)
    cv2.putText(result, f"{real_w:.1f} cm",
                (x + w // 2 - 40, y - 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # линия высоты (слева)
    cv2.line(result, (x - 20, y), (x - 20, y + h), (0, 255, 0), 2)
    cv2.putText(result, f"{real_h:.1f} cm",
                (x - 80, y + h // 2),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return result