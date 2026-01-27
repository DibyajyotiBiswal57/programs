#Q47

import urllib.request
import json

def get_usd_to_inr_rate():
    # Reliable free API for exchange rates
    url = "https://open.er-api.com/v6/latest/USD"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    return data['rates']['INR']

def convert_usd_to_inr(amount_usd):
    rate = get_usd_to_inr_rate()
    amount_inr = amount_usd * rate
    return amount_inr, rate

if __name__ == "__main__":
    usd = float(input("Enter amount in USD: "))
    inr, rate = convert_usd_to_inr(usd)
    print(f"Current USD to INR rate: {rate:.2f}")
    print(f"{usd} USD = {inr:.2f} INR")
