#LOPEZ M4P1.py 10/25/2026
# input section
f = open("students.txt", "r")
lastname = f.readline().strip()

# processing section
total_tuition = 0
count = 0

print("Last Name       Credits       Tuition")

while lastname != "":
    district = f.readline().strip()
    credits = int(f.readline())

    if district == "I":
        cost = 250
    else:
        cost = 500

    tuition = credits * cost

    total_tuition = total_tuition + tuition
    count = count + 1

    # output section
    print(f"{lastname:<15}{credits:<14}${tuition:>10,.2f}")

    lastname = f.readline().strip()

f.close()

print()
print(f"Total tuition owed: ${total_tuition:,.2f}")
print("Number of students:", count)