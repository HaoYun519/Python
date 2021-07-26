# 抓取 kkday.COM 的文章資料
import urllib.request as req
# 找到正確的Headers >> Request URL
url="https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=a25577f029af5b8ba10d4f71d9caa2bb"
# 建立一個 Request 物件, 附加 Request Headers 的資訊
request=req.Request(url, headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") #根據觀察, 取得的資料是 JSON 格式

# 解析 JSON 格式的資料, 取得每篇文章的標題
import json

# data=data.replace("])}while(1);</x>","") # 
# 將除了JSON 格式以外的資料清乾淨 Response 可以檢查

data=json.loads(data) # 把原始的 JSON 資料解析成字典/列表的表示形式
# 取得 JSON 資料中的文章標題
p=1
while p<7: 
    posts=data["data"]["homepage_product_group"][p]["title"] # 用 Preview 分析位址
    print("熱門推薦 : "+posts)
    p += 1
