from math import sin
import math

def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    area = (((circle_radius ** 2 * number_of_sides) * sin((360 / number_of_sides) * math.pi / 180)) / 2)
    return round(area, 3)
