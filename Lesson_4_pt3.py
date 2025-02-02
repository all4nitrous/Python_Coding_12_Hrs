item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity =  int(input(f"How many {item} would you like?: "))
total = price * quantity

print("********************************************")
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")
print("********************************************")

#print("********************************************")
#print(f"You have bought {quantity} {item} making your total ${total}")
#print("********************************************")