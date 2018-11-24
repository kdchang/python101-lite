import requests

resp = requests.get('http://www.twse.com.tw/exchangeReport/BWIBBU?response=json&date=20181115&stockNo=2330&_=1542243610772')

print(resp.json())
