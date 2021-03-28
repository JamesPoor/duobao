import threading, requests, time, json
import mysql.connector

def find(jd, one):
    while True:
        time.sleep(5)
        http_data = requests.get("http://query.shuzhikj.com/api/platform/get_taskrank?id=" + jd['data'], headers=headers)
        http_json = json.loads(http_data.text)
        if http_json['code'] == 0:
            print('任务》》', '关键词：', one[3], http_data.text)
        else:
            print("[查询成功]任务排名为:", http_json['data'], "原始数据为:", http_data.text)
            cursor.execute('update task set status = 2,rank = ' + str(http_json['data']) + ' where id=' + str(one[0]))
            print('one为：', one[1], 'data为：', http_json['data'])
            updata_rank = "https://t.idccap.com/api/v1/QuickRanking/updata_rank"
            payload = {
                'id': one[1],
                'rank': http_json['data']
            }
            http_data = requests.post(url=updata_rank, data=payload)
            http_text = http_data.text
            print('传输成功:', http_text)
            break

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'duobao',
    'password': 'wasd123',
    'database': 'duobao'
}
con = mysql.connector.connect(**config)

cursor = con.cursor()
sq = 'select * from task where status = 0 or status = 3'
cursor.execute(sq)
taskList = cursor.fetchall()
cursor.close()
print("tasklist_______", taskList)
for one in taskList:
    name = one[3]
    url = one[2]
    print(one)
    url = 'http://query.shuzhikj.com/api/platform/add_task?name=' + str(name) + '&url=' + str(url) + '&type=1&urlmode=1'
    headers = {
        'apikey': 'mJDNNXnsu946MLB'
    }
    http_data = requests.get(url=url, headers=headers)
    http_text = http_data.text
    json_data = json.loads(http_text)
    print('任务》》', '关键词：', one[3], http_text)
    for _ in range(3):
        threading.Thread(target=find, args=(json_data,one)).start()

con.close()
