import math 
x = float(input("Enter value for x:"))
y = float(input("Enter a value for y:"))
z = float(input("Enter a value for z:"))
first_result = math.pow(x,z)
second_result = math.pow(x,(math.pow(y,z)))
third_result = math.fabs(x - y)
fourth_result = math.sqrt(math.pow(x,z))
print(f"{first_result:.2f} {second_result:.2f} {third_result:.2f} {fourth_result:.2f}")
