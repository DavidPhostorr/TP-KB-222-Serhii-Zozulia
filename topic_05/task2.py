import requests

value = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")

for elem in value.json():
    if elem['cc'] in ['EUR' , 'USD' , 'PLN']:
        print(elem['cc'], "  ", elem['rate'])
    