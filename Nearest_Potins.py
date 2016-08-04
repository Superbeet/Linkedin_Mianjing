import heapq

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

class PointsOnAPlane():
	def __init__(self):
		self.points = []

	def add_point(self, point):
		self.points.append(point)

	def find_nearest(self, center, p):
		
		def cal_distance(center, point):
			distance = ((point.x-center.x)**2 + (point.y-center.y)**2)//2
			return distance

		self.maxheap = []
		heapq.heapify(self.maxheap)
		
		size = 0

		for point in self.points:
			dist = -cal_distance(center, point)
			if size < p:
				heapq.heappush(self.maxheap, (dist, point))
				size += 1
			else:
				# dist = cal_distance(center, point) 
				if dist > self.maxheap[0][0]:
					heapq.heapreplace(self.maxheap, (dist, point))

		res = []
		for i in xrange(size):
			point = heapq.heappop(self.maxheap)
			print [point[1].x, point[1].y], -point[0]
			res.append([point[1].x, point[1].y])

		return res


sol = PointsOnAPlane()
sol.add_point(Point(1,2))
sol.add_point(Point(5,2))
sol.add_point(Point(4,2))
sol.add_point(Point(6,2))
center = Point(2,2)
print sol.find_nearest(center, 2)