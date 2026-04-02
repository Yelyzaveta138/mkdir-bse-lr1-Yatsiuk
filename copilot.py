# Create a function that calculates the square area and returns a formatted string
def calculate_square_area(side_length):
    area = side_length ** 2
    return f"The area of the square with side length {side_length} is {area}."          

print(calculate_square_area(5))
