# If Else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
        bill += 5
    elif age <= 18:
        print("Please pay $7.")
        bill += 7
    elif age > 18:
        print("Please pay $12.")
        bill += 12
    #     age >= 45 and age <= 55
    elif 45 <= age <= 55:
        bill += 0

    photo = input("Do you want photos? yes/no ")
    if photo == "yes":
        bill += 3
        print(bill)
    if photo == "no":
        print(bill)

else:
    print("Sorry you have to grow taller before you can ride.")


# Modulo
angka = int(input("Inputkan Angka? "))
if angka % 2 == 0 :
    print("Angkanya Genap")
else:
    print("Angkanya Ganjil")

# Pizza Python Delivery
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
else:
    print("The Size Unavailable")

print(f"Your total bill is ${bill}")