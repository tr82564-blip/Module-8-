#LOPEZ M4P1.py 10/25/2026
# input section
p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate: "))

# processing section
total_interest = 0

print()
print("Year     Beginning       Ending")
print("          Balance        Balance")

for year in range(1, 6):
    i = p * r
    eb = p + i
    total_interest = total_interest + i

    # output section
    print(f"{year:<8} ${p:>10,.2f}    ${eb:>10,.2f}")

    p = eb

print()
print(f"Total interest earned: ${total_interest:,.2f}")