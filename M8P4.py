#LOPEZ M4P1.py 10/25/2026
# input section
from pathlib import Path

f = open(Path(__file__).with_name("items.txt"), "r")
item = f.readline().strip()

# processing section
total_price = 0
count = 0

print("Item          Quantity       Price       Extended Price")

while item != "":
    qty = float(f.readline())
    price = float(f.readline())

    ep = qty * price

    total_price = total_price + ep
    count = count + 1

    # output section
    print(f"{item:<14}{qty:<12.0f}${price:>10,.2f}       ${ep:>10,.2f}")

    item = f.readline().strip()

f.close()

if count > 0:
    avg = total_price / count
else:
    avg = 0

print()
print(f"Total extended prices: ${total_price:,.2f}")
print("Number of orders:", count)
print(f"Average order: ${avg:,.2f}")