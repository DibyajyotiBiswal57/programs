#Q11
print("This program calculates profit and profit% or loss and loss%")
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

profit = selling_price - cost_price

if profit > 0:
    print("Profit: ", profit)
    print("Profit%: ", (profit/cost_price)*100)
elif profit < 0:
    print("Loss: ", -profit)
    print("Loss%: ", (-profit/cost_price)*100)
else:
    print("No profit or loss")
