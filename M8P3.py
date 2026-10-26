#LOPEZ M4P1.py 10/25/2026
# input section
from pathlib import Path

f = open(Path(__file__).with_name("employees.txt"), "r")
lastname = f.readline().strip()

# processing section
total_bonus = 0

print("Last Name        Salary          Bonus")

while lastname != "":
    salary = float(f.readline())

    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate
    total_bonus = total_bonus + bonus

    # output section
    print(f"{lastname:<15} ${salary:>10,.2f}    ${bonus:>10,.2f}")

    lastname = f.readline().strip()

f.close()

print()
print(f"Total bonuses paid: ${total_bonus:,.2f}")