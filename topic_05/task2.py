import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
response = requests.get(url)
data = response.json()

rates = {item["cc"]: item["rate"] for item in data}
while True:
    
    amount = float(input("Enter amount of money: "))
    currency = input("Enter the code of the currency you want to transfer to:").upper()

    if currency not in rates:
        print("Currency not found")
    else: 
        converted = amount * rates[currency]
        print(f"{amount} {currency} = {converted} UAH")
        