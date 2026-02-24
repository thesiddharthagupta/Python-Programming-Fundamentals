menu = {1:40, 2:50, 3:45, 4:55}

total_bill = 0

while True:
    choose = int(input("Enter choice: "))
    quantity = int(input("Enter quantity: "))

    if choose in menu:
        total_bill += menu[choose] * quantity
    else:
        print("Invalid choice")

    if input("Order more? (yes/no): ").lower() != "yes":
        break

tax = total_bill * 0.08
Finalbill = total_bill + tax

print("-------------")
print("total before tax:", total_bill)
print("8% Tax", tax)
print("Final Bill Amount: ", Finalbill)
