
cp = float(input("Enter the cost price: "))
#10% discount if the amount is above 10000 else a discount of 7.5%.
if cp > 10000:
    discount = cp * 10/100
    sp = cp - discount
    print(f"{discount} is the disount amount.")
    print(f"{sp} is the selling price.")
elif cp < 10000:
    discount = cp * 7.5/100
    sp = cp - discount
    print(f"{discount} is the disount amount.")
    print(f"{sp} is the selling price.")
