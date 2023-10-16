from operator import itemgetter
import requests

value = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")

data = value.json()

rates = {item["cc"]: item["rate"] for item in data}

money = float(input("Enter amount of money: "))
fromm = input("Enter the code of the currency in which the amount is located: ")
to = input("Enter the code of the currency you want to transfer to: ")

if fromm not in rates or to not in rates:
    print("Currency not found")
else:
    converted = money * (rates[to] / rates[fromm])
    print(f"{money} {fromm} = {converted} {to}")
