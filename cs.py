import threading, requests, json
import mysql.connector

def find(jd, one):
    if jd:
        json_data = json.loads(requests.get("http://query.shuzhikj.com/api/platform/get_taskrank?id=" + jd['data'], headers=headers).text)
        while json_data['code'] == 0:
            json_data = json.loads(requests.get("http://query.shuzhikj.com/api/platform/get_taskrank?id=" + jd['data'], headers=headers).text)
        else:
            print("[查询成功]任务排名为:", json_data['data'], "原始数据为:", json_data)
            config = {
                'host': 'localhost',
                'port': 3306,
                'user': 'duobao',
                'password': 'wasd123',
                'database': 'duobao'
            }
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            cursor.execute('update task set status=2, rank=' + str(json_data['data']) + ' where id=' + str(one[0]))
            print('传输成功:', requests.post(url="https://t.idccap.com/api/v1/QuickRanking/updata_rank", data={'id': one[1], 'rank': json_data['data']}).text)

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'duobao',
    'password': 'wasd123',
    'database': 'duobao'
}
con = mysql.connector.connect(**config)
cursor = con.cursor()
cursor.execute('select * from task where status = 0 or status = 3')
taskList = cursor.fetchall()
headers = {
    'apikey': 'mJDNNXnsu946MLB'
}
for one in taskList:
    url = 'http://query.shuzhikj.com/api/platform/add_task?name=' + str(one[3]) + '&url=' + str(one[2])+'&type=1&urlmode=1'
    json_data = json.loads(requests.get(url=url, headers=headers).text)
    print('任务 >> ', '关键词：', one[3], json_data)
    for _ in range(3):
        threading.Thread(target=find, args=(json_data, one)).start()
con.close()
