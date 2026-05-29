import cv2
from utils.detectSize import detectSize
from utils.findContours import findContours
from utils.drawSize import draw_box_size
from utils.get_top_x_from_contour import get_top_x_from_contour
from utils.calculate_box_height import calculate_box_height
from utils.resizeShape import resizeShape

def main():
    image1 = cv2.imread("./../img/box/cam3.png")
    image2 = cv2.imread("./../img/box/cam4.png")
    image2 = image2[200:image2.shape[1]]

    count = 0
    while True:
        contours1 = findContours(image1)
        contours2 = findContours(image2)

        if contours1 and contours2 and count==0:

            cnt1 = contours1[1]
            cnt2 = contours2[1]
            cnt1_main = max(contours1, key=cv2.contourArea)
            cnt2_main = max(contours2, key=cv2.contourArea)
            x1_top_box, y1_top_box = get_top_x_from_contour(cnt1_main)
            x2_top_box, y2_top_box = get_top_x_from_contour(cnt2_main)
            x1_top, y1_top = get_top_x_from_contour(cnt1)
            x2_top, y2_top = get_top_x_from_contour(cnt2)

            height = calculate_box_height(y1_top_box, y2_top_box,y1_top, y2_top)
            print(f"Высота коробки: {height:.2f} см")
            cm_per_px = 1/24

            result_image1 = draw_box_size(image1, cnt1_main, cm_per_px)
            result_image2 = draw_box_size(image2, cnt2_main, cm_per_px)

            cv2.circle(result_image1, (x1_top, y1_top), 10, (0, 0, 255), -1)
            cv2.circle(result_image2, (x2_top, y2_top), 10, (0, 0, 255), -1)

            cv2.circle(result_image1, (x1_top_box, y1_top_box), 10, (0, 255, 0), -1)
            cv2.circle(result_image2, (x2_top_box, y2_top_box), 10, (0, 255, 0), -1)
            count+=1

            detectSize(contour=cnt1_main,cm_per_px=cm_per_px)
            detectSize(contour=cnt1_main,cm_per_px=cm_per_px)
            detectSize(contour=cnt1,cm_per_px=cm_per_px)

            cv2.imshow("Original1", resizeShape(result_image1))
            cv2.imshow("Original2", resizeShape(result_image2))
        key = cv2.waitKey(1) & 0xFF

        # Нажмите ESC для выхода
        if key == 27:
            break

        # Нажмите S, чтобы сохранить результат
        if key == ord("s"):
            print("\nИзображения сохранены.")

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()