# defining a fucntion to calculate area of a rectangle
def calculate_rectangle_area(l,w):
    area = l * w
    return area

l_input= float(input("enter the lenght of the rectangle:"))
w_input= float(input("enter the width of the rectangle:"))

area_result = calculate_rectangle_area(l_input,w_input)
print(f"area of rectangle is {area_result} square units")