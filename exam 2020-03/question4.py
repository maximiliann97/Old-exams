import numpy as np
import abc


class Shape(metaclass=abc.ABCMeta):
    def __init__(self, centre):
        self.centre = centre

    def move(self, translation_vector):
        self.centre += translation_vector

    @abc.abstractmethod
    def resize(self, scale):
        pass

    @abc.abstractmethod
    def rotate(self, theta):
        pass

    @abc.abstractmethod
    def bounding_box(self):
        pass


class Circle(Shape):
    def __init__(self, radius, centre):
        super().__init__(centre)
        self.radius = radius

    def resize(self, scale):
        self.radius *= scale

    def rotate(self, theta):
        pass

    def bounding_box(self):
        return self.centre - self.radius, self.centre + self.radius


class Polygon(Shape):
    def __init__(self, points):
        centre = np.mean(points, axis=0)
        super().__init__(centre)
        self.points = points - centre

    def resize(self, scale):
        self.points *= scale

    def rotate(self, theta):
        m = np.array([[np.cos(theta), -np.sin(theta)],
                      [np.sin(theta), np.cos(theta)]])
        self.points = np.dot(m, self.points.T).T

    def bounding_box(self):
        return self.centre + np.min(self.points, axis=0), self.centre + np.max(self.points, axis=0)


class Rectangle(Polygon):
    def __init__(self, lower_left_corner, width, height, centre):
        super().__init__(centre)
        self.lower_left_corner = lower_left_corner
        self.width = width
        self.height = height

    def build(self):
        return


global_points = np.array([
    [0.0, 0.0],
    [3.0, 1.0],
    [2.0, 1.5],
    [1.0, 3.0],
])

poly = Polygon(global_points)
print(f'Polygon with centre at {poly.centre} and bounding box {poly.bounding_box()}')
print(f'Its first point is at {poly.points[0]} relative to its centre')
poly.move(np.array([-0.2, 0.3]))
poly.resize(2.0)
print(f'Polygon with centre at {poly.centre} and bounding box {poly.bounding_box()}')
poly.rotate(np.pi) # rotate 180 degrees
print(f'Polygon with centre at {poly.centre} and bounding box {poly.bounding_box()}')