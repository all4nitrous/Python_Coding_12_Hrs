#Lesson on user input

name = input("What is your name?: ")
print("********")
age = int(input("How old are you?: "))

#age = int(age) #Needed to convert from string to integer
age = age + 1

print("********")
print(f"Hello {name}!")
print("********")
print("Happy Birthday!")
print("********")
print(f"You are {age} years old!")
print("********")