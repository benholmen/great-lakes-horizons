import cv2
import numpy as np
import math
import imutils

def find_horizon(img_filename):
	img = cv2.imread(img_filename)
	edges = cv2.Canny(img, 100, 200)
	lines = cv2.HoughLinesP(edges, 1, math.pi / 180.0, 100, minLineLength=150, maxLineGap=25)

	angles = []
	horizon_y = []

	for x1, y1, x2, y2 in lines[0]:
		# cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
		angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
		angles.append(angle)
		horizon_y.append(y1)
		horizon_y.append(y2)

	median_angle = np.median(angles)
	median_horizon_y = np.median(horizon_y)

	img_rotated = imutils.rotate(img, median_angle)
	img_cropped = img_rotated
	cv2.imwrite('output.jpg', img_cropped)

	return median_angle

def calculate_rotation(coordinates):
	(x1, y1) = coordinates['left']
	(x2, y2) = coordinates['right']
	slope = (y2 - y1) / (x2 - x1)
	return math.degrees(math.atan(slope))

img_filename = 'test1.jpg';

horizon_coordinates = find_horizon(img_filename)
print(img_filename)
print(horizon_coordinates)
# rotation = calculate_rotation(horizon_coordinates)
# print(rotation)
