import requests
import json


page_id = 'PAGE_ID' # 欲爬取 fans page id
access_token = 'YOUR_ACCESS_TOKEN' # 先到 https://developers.facebook.com/ 註冊一個 app，然後申請 Page Public Content Access 權限，之後可以從 https://developers.facebook.com/tools/explorer 取得 token
limit = 5  # 限制資料筆數

response = requests.get('https://graph.facebook.com/v3.2/{}?limit={}fields=id,posts&access_token={}'.format(page_id, limit, access_token))
print(response.json())
