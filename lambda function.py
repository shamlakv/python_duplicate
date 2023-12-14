square_area=lambda length:length**2
rectangle_area=lambda length,width:length*width
triangle_area=lambda base,height:0.5*base*height

length = int(input("Enter the length of the square: "))
square_area=square_area(length)
print("The area of the square is:", square_area)
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle : "))
rectangle_area=rectangle_area(length,width)
print("The area of the rectangle is:", rectangle_area)
base =float (input("Enter the base  of the triangle: "))
height = float(input("Enter the height of the triangle: "))

triangle_area = triangle_area(base, height)
print("The area of the triangle is:",triangle_area)
