# Input total liabilities and shareholders' equity
total_liabilities = float(input("Enter the total liabilities: "))
shareholders_equity = float(input("Enter the total shareholders' equity: "))

# Calculate the Debt-to-Equity (D/E) ratio
if shareholders_equity != 0:
    debt_to_equity_ratio = total_liabilities / shareholders_equity
    print(f"The Debt-to-Equity (D/E) ratio is: {debt_to_equity_ratio:.2f}")
else:
    print("Shareholders' equity cannot be zero. Please enter a valid number.")
