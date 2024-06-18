import unittest
from geometry import rectangle_area, rectangle_perimeter, circle_area, circle_circumference

class TestCalc(unittest.TestCase):
	def test_rec_area(self):
		self.assertEqual(rectangle_area(4,4), 16)
		self.assertEqual(rectangle_area(1,1), 1)
		self.assertEqual(rectangle_area(7,0), 0)
	def test_rec_per(self):
		self.assertEqual(rectangle_perimeter(3,6), 18)
		self.assertEqual(rectangle_perimeter(6,0.5), 13)
		self.assertEqual(rectangle_perimeter(3,0), 6)

	def test_circle_area(self):
		self.assertEqual(circle_area(5), 78.5)
		self.assertEqual(circle_area(1), 3.14)
		self.assertEqual(circle_area(0), 0)
	def test_circle_circ(self):
		self.assertEqual(circle_circumference(3), 18.84)
		self.assertEqual(circle_circumference(1), 6.28)
		self.assertEqual(circle_circumference(0), 0)

if __name__ == '__main__':
	unittest.main()
