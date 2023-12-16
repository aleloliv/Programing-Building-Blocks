import math

square_side = float(input("What is the length of a side of the square in centimeters? "))

square_area = square_side * square_side
square_area_meters = square_area / 10000

print(f"The area of the square is: {square_area} cm² or {square_area_meters} m²")


rectangle_length = float(input("What is the length of rectangle in centimeters? "))
rectangle_width = float(input("What is the width of the rectangle in centimeters? "))

rectangle_area = rectangle_length * rectangle_width
rect_area_meters = rectangle_area / 10000

print(f"The area of the rectangle is: {rectangle_area} cm² or {rect_area_meters} m²")


circle_radius = float(input("What is the radius of the circle in centimeters? "))

circle_area = circle_radius * circle_radius * math.pi
circle_area_meters = circle_area / 10000

print(f"The area of the circle is: {circle_area} cm² or {circle_area_meters} m²")


length = float(input("Please type a value of length: "))

square2_area = length ** 2

circle2_area = square2_area * math.pi

cube_volume = length ** 3

sphere_volume = length ** 3 * math.pi * (4 / 3)

print(f"The area of the square is: {square2_area} cm²\nThe area of the circle is: {circle2_area} cm²\nThr volume of the cube is: {cube_volume} cm³\nThe volume of the sphere is: {sphere_volume} cm³")
