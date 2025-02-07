# Python Weight Converter
while True:
    unit = input("Kilograms or Pounds? (K or L): ").strip().lower()


    if unit == "k":
        weight = float(input("Enter your weight: "))
        weight = weight * 2.205
        unit = "lbs."
        print(f"Your weight is: {round(weight, 2)} {unit}")
        break;
    elif unit == "l":
        weight = float(input("Enter your weight: "))
        weight = weight / 2.205
        unit = "Kgs."
        print(f"Your weight is: {round(weight, 2)} {unit}")
        break;
    else:
        print(f"{unit} was not valid")


