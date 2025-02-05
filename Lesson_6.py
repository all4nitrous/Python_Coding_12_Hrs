#Arithmetic Operators

import math

friends = 10

#friends += 1
#friends -= 2
#friends *= 3
#friends /= 2
#friends **= 2
remainder = friends % 3

print(friends)

print("*****************")

x = 3.14
y = 4
z = 5

#result = round(x)
#result = abs(y) #Distance to 0
#result = pow(4, 3)
#result = max(x, y, z)
result = min(x, y, z)

print(result)

print("*****************")

#print(math.pi)

x = 9.9

#result = math.sqrt(x)
#result = math.ceil(x) #Rounds up the number
result = math.floor(x)


print(result)

print("*****************")

radius  = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius

print(f"The circumference is: {circumference}")

print("*****************")

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm^2")

print("*****************")

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")

