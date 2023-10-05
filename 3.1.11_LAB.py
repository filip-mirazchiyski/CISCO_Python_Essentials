income = float(input())

tax = 0

if 0 < income <= 85528:
    tax = 0.18 * income - 556.02
elif income > 85528:
    tax = 14839.02 + 0.32 * (income - 85528)
else:
    tax = 0.0


print(f"The tax is: {(round(tax, 5))} thalers")
print(f"The tax is: {(round(tax, 4))} thalers")
print(f"The tax is: {(round(tax, 3))} thalers")
print(f"The tax is: {(round(tax, 2))} thalers")
print(f"The tax is: {(round(tax, 1))} thalers")
print(f"The tax is: {(round(tax, 0))} thalers")
print(f"The tax is: {(round(tax, 5))} thalers")
print(f"The tax is: {tax} thalers")
