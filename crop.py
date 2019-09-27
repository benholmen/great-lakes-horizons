import Algorithmia
import math
import base64

def find_horizon(img_filename):
	algo = client.algo("ukyvision/deephorizon/0.1.0")
	image = base64.b64encode(open(img_filename, "rb").read()).decode('utf-8')
	return algo.pipe({'image':'data:image/jpg;base64,'+image}).result

	coords = dict()
	coords['left'] = [-3000, -4151.762398470525]
	coords['right'] = [3000, -4162.500768085014]
	return coords

def calculate_rotation(coordinates):
	(x1, y1) = coordinates['left']
	(x2, y2) = coordinates['right']
	slope = (y2 - y1) / (x2 - x1)
	return math.degrees(math.atan(slope))

algorithmia_api_key = 'simqxKqiI+a2IwUlt7Rn5eaxNoQ1'
img_filename = 'test4.jpg';

client = Algorithmia.client(algorithmia_api_key)

horizon_coordinates = find_horizon(img_filename)
print(horizon_coordinates)
rotation = calculate_rotation(horizon_coordinates)
print(rotation)
