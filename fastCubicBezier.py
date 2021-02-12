class fastCubicBezier:

	""" 
	calculates Bezier points using the forward difference method
	Source: https://www.drdobbs.com/forward-difference-calculation-of-bezier/184403417?pgno=1
		
	This method is way faster then using the formula P(x,y) = (1−t)³p1 + 3t(1−t)²p2 + 3t²(1−t)p3 + t³p4	
	
	p1x, p1y is the start point
	p2x, p2y is the end point
	
	h1x, h1y, h2x, h2y are the control points
	
	resolution is the stepping
	"""

	def universal(p1x, p1y, p2x, p2y, h1x, h1y, h2x, h2y, resolution):

		t = 1 / resolution

		ax = -p1x + 3*h1x - 3*h2x + p2x
		ay = -p1y + 3*h1y - 3*h2y + p2y

		bx = 3*p1x -6*h1x + 3*h2x
		by = 3*p1y -6*h1y + 3*h2y

		cx = -3*p1x + 3*h1x
		cy = -3*p1y + 3*h1y

		dx = p1x
		dy = p1y


		point_x = dx
		point_y = dy

		# express standard cubic bezier formular as at³ + bt² + ct + d
		x = ax*t**3 + bx*t**2 + cx*t + dx
		y = ay*t**3 + by*t**2 + cy*t + dy

		# 1nd derivation
		d1x = 6 * ax * (t**3) + 2 * bx * (t**2)
		d1y = 6 * ay * (t**3) + 2 * by * (t**2)

		# 2rd derivation
		d2x = 6 * ax * (t**3)
		d2y = 6 * ay * (t**3)
			
		points_X = [point_x]
		points_Y = [point_y]

		for i in range(resolution):
			point_x += x
			point_y += y
			
			x += d1x
			y += d1y
			
			d1x += d2x
			d1y += d2y

			points_X.append(point_x)
			points_Y.append(point_y)
			
		return points_X, points_Y


	def animation(h1x, h1y, h2x, h2y, resolution):
		# p1 and p2 are 0 and 1, so we can stripe the code

		t = 1 / resolution

		ax = 3*h1x - 3*h2x + 1
		ay = 3*h1y - 3*h2y + 1

		bx = -6*h1x + 3*h2x
		by = -6*h1y + 3*h2y

		cx = 3*h1x
		cy = 3*h1y

		point_x = 0
		point_y = 0

		# express standard cubic bezier formular as at³ + bt² + ct + d
		x = ax*t**3 + bx*t**2 + cx*t
		y = ay*t**3 + by*t**2 + cy*t

		# 2nd derivation
		d1x = 6 * ax * (t**3) + 2 * bx * (t**2)
		d1y = 6 * ay * (t**3) + 2 * by * (t**2)

		# 3rd derivation
		d2x = 6 * ax * (t**3)
		d2y = 6 * ay * (t**3)
			
		points_X = [point_x]
		points_Y = [point_y]

		for i in range(resolution):
			point_x += x
			point_y += y
			
			x += d1x
			y += d1y
			
			d1x += d2x
			d1y += d2y

			points_X.append(point_x)
			points_Y.append(point_y)
			
		return points_X, points_Y




print (fastCubicBezier.animation(0.732,0,0.26,1, 10)[1])
print (fastCubicBezier.universal(0,0, 1,1,0.732,0,0.26,1, 10)[1])



