def calculate_box_height(y1_top, y2_top, y1_ref, y2_ref):
    Z_plane = 100.0
    d_plane = abs(y1_ref - y2_ref)
    d_top = abs(y1_top - y2_top)
    Z_top = Z_plane * d_plane / d_top
    height = Z_plane - Z_top

    return height