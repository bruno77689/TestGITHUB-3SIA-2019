import cv2
import numpy as np

def midpoint_line(img, x0, y0, x1, y1, color, thickness):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    d = 2 * dy - dx
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)
    y = y0

    for x in range(x0, x1):
        cv2.line(img, (x, y), (x, y), color, thickness)

        if (d > 0):
            d = d + incrNE;
            y = y +1
        else:
            d = d + incrE
            
    cv2.line(img, (x, y), (x, y), color, thickness)
    
    return

BLACK = (0, 0, 0)
THICKNESS = 3
CORNERS_SQUARE_01 = [(20, 200), (100, 200), (20, 280), (100, 280)]
CORNERS_SQUARE_02 = [(70, 150), (150, 150), (70, 230), (150, 230)]

canvas = np.ones((300, 400, 3)) * 255

cv2.line(canvas, CORNERS_SQUARE_01[0], CORNERS_SQUARE_01[1], BLACK, THICKNESS)
cv2.line(canvas, CORNERS_SQUARE_01[0], CORNERS_SQUARE_01[2], BLACK, THICKNESS)
cv2.line(canvas, CORNERS_SQUARE_01[1], CORNERS_SQUARE_01[3], BLACK, THICKNESS)
cv2.line(canvas, CORNERS_SQUARE_01[3], CORNERS_SQUARE_01[2], BLACK, THICKNESS)

cv2.line(canvas, CORNERS_SQUARE_02[0], CORNERS_SQUARE_02[1], BLACK, THICKNESS)
cv2.line(canvas, CORNERS_SQUARE_02[0], CORNERS_SQUARE_02[2], BLACK, THICKNESS)
cv2.line(canvas, CORNERS_SQUARE_02[1], CORNERS_SQUARE_02[3], BLACK, THICKNESS)
cv2.line(canvas, CORNERS_SQUARE_02[3], CORNERS_SQUARE_02[2], BLACK, THICKNESS)

midpoint_line(canvas, CORNERS_SQUARE_01[0][0], CORNERS_SQUARE_01[0][1], CORNERS_SQUARE_02[0][0], CORNERS_SQUARE_02[0][1], BLACK, THICKNESS)

cv2.line(canvas, CORNERS_SQUARE_01[1], CORNERS_SQUARE_02[1], BLACK, THICKNESS)
cv2.line(canvas, CORNERS_SQUARE_01[2], CORNERS_SQUARE_02[2], BLACK, THICKNESS)
cv2.line(canvas, CORNERS_SQUARE_01[3], CORNERS_SQUARE_02[3], BLACK, THICKNESS)

cv2.imshow("001", canvas)
