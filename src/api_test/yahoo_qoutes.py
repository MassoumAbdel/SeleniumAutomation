import requests

url = "https://query1.finance.yahoo.com/v8/finance/cart/AAPL"

payload = {}
headers = {}

response = requests.request("Get", url, headers=headers, data=payload)

print(response.status_code)
print(response.content)
print(response.text)

