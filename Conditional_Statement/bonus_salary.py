employee = input("Enter your role (m for manager, e for employee): ").lower()

salary = int(input("Enter your salary: "))
years = int(input("Enter your work experience: "))

if employee == 'm':
    bonus = salary * (0.05 + 0.07 + 0.10)
    print(f"You got {bonus:.2f} bonus")

elif years >= 3:
    bonus = salary * (0.05 + 0.07)
    print(f"You got {bonus:.2f} bonus")

else:
    print("No Bonus")