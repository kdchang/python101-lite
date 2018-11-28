import pandas as pd


# 讀取資料，這邊讀取本期發布之不動產買賣實價登錄批次資料 https://data.gov.tw/dataset/25119：注意資料集可能會更新，但觀念類似
# 使用 google sheet 觀看，參考資料集 https://docs.google.com/spreadsheets/d/1hCnDQlzyQBScElPe2sGiJmcpGn8DPiQOuKT73rTEbYM/edit#gid=0
# 該檔案為 utf-8 編碼，使用編碼使用 utf-8 讀取 csv 檔案成 pandas 的 DataFrame 結構
raw_data_frame = pd.read_csv('./lvr_landAcsv/a_lvr_land_a.csv', encoding='utf-8')

# drop 可以 drop 掉不要的資料 row 列，這邊把第一列英文 drop 掉，row index 是從 0 開始，所以 drop 0:1，不含 1
# reset_index 是讓 drop 後可以重新 reset row 列的 index
# drop=True 避免之前的舊的 index 變成一個欄位
data_frame = raw_data_frame.drop(raw_data_frame.index[0:1]).reset_index(drop=True)

# 可以看出來 dtype 為 object
print('dtype', data_frame.loc[:, ['土地移轉總面積平方公尺', '建物移轉總面積平方公尺']].dtypes)

# 使用 loc 來 filter 出我們想要的欄位（因為有些不適合計算平均值），loc[列範圍, 欄範圍]，這邊取所有列 row 也就是所取得 土地移轉總面積平方公尺', '建物移轉總面積平方公尺 的所有資料
raw_num_df = data_frame.loc[:, ['土地移轉總面積平方公尺', '建物移轉總面積平方公尺']]
# apply 是一種將函式 apply 用到多的欄位的用法，這邊意思是把 土地移轉總面積平方公尺', '建物移轉總面積平方公尺 值從原本的 string object dtype 轉成數字，當發生無法轉換時忽略：errors='ignore'
num_df = raw_num_df.apply(pd.to_numeric, errors='ignore')
print('num_df', num_df.mean())
