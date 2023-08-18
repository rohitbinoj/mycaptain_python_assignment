radius = float(input("Enter radius of circle: "))
if radius < 0:
    print("Radius cannot be negative")
else:
    area = 3.14159 * radius * radius
    print(f"The area of the circle is {area}")
