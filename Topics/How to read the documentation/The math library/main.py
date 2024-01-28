import math

def calculate_cosine(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    cosine_result = math.cos(angle_radians)
    rounded_cosine = round(cosine_result, 2)
    print(rounded_cosine)

# You don't need to call the function here, just implement it as mentioned in the problem.
