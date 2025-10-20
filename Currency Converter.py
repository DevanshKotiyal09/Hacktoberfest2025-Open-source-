rates = {"USD": 1, "INR": 83.5, "EUR": 0.91}
amount = float(input("Enter amount in USD: "))
for currency, rate in rates.items():
    print(f"{amount} USD = {amount * rate} {currency}")
