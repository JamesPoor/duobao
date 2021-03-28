import requests
import json

updata_rank = "https://t.idccap.com/api/v1/QuickRanking/updata_rank"
payload = {
    'id': 3,
    'rank': 14
}
http_data = requests.post(url=updata_rank, data=payload)
http_text = http_data.text
# 将json格式数据转换为字典
json_data = json.loads(http_text)
print('传输成功:', http_data.text)

# payload = 'id=3&rank=17'
# headers = {}
# response = requests.request("POST", updata_rank, headers=headers, data=payload)
# print('传输成功:', response.text)