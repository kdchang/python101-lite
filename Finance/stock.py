import requests
import pandas as pd

"""
本範例根據證交所個股日本益比、殖利率及股價淨值比(以個股月查詢) 實作
http://www.twse.com.tw/zh/page/trading/exchange/BWIBBU.html
"""
# 查詢時間
date = '20181115'
# 股票代號
stock_number = '2330'
# 發出 http request 請求
request_url = 'http://www.twse.com.tw/exchangeReport/BWIBBU?response=json&date={}&stockNo={}&_=1542243610772'.format(date, stock_number)
response = requests.get(request_url)

# 將取得 json 格式結果轉成 python dict 字典格式
raw_data = response.json()
# 取出標題
fields = raw_data['fields']
# 其中 data 這個 key 所對應的值為主要我們想要的 股日本益比、殖利率及股價淨值比 資料
data = raw_data['data']
print(data)

# 將資料轉換成 pandas DataFrame 格式，並使用取出的 fields 當作標題
result = pd.DataFrame(data, columns=fields)    
print('result', result)

# 輸出成 .csv 檔案
result.to_csv('./stock.csv', encoding='utf-8')
