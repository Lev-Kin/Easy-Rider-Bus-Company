def compare(numerator, denominator):
    if denominator == 0:
        return False
    return numerator / denominator == 0.5


a = int(input())
b = int(input())

result = compare(a, b)
if result:
    print("True")
else:
    print("False")
