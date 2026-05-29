import numpy as np

def get_top_center_from_contour(cnt, band_px=10):
    points = cnt.reshape(-1, 2)

    # находим самый верх
    min_y = np.min(points[:, 1])

    # берём полосу верхних точек
    top_points = points[points[:, 1] <= min_y + band_px]

    # считаем центр
    x_center = int(np.mean(top_points[:, 0]))
    y_center = int(np.mean(top_points[:, 1]))

    return x_center, y_center