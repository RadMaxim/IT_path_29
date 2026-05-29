import numpy as np
def get_top_x_from_contour(cnt):
    points = cnt.reshape(-1, 2)
    top_point = points[np.argmin(points[:, 1])]
    x_top = int(top_point[0])
    y_top = int(top_point[1])
    return x_top, y_top