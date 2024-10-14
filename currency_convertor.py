def currency_convertor(currency, amount, rate):
    return amount * rate

currency = (input("Enter the currency: "))
amount = float(input(f"Enter the ammount of {currency}: "))
rate = float(input(f"Enter the rate of converting {currency} to USD: "))

converted_amount = currency_convertor(currency, amount, rate)
print ("%s %s coverted to USD is equals to %s", amount, currency, converted_amount)