import mysql
from mysql.connector import cursor

if __name__ == '__main__':

    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'duobao',
        'password': 'wasd123',
        'database': 'duobao'
    }
    con = mysql.connector.connect(**config)
    # 创建游标，用于执行mysql语句，并且查询结果会一并保存游标之中。
    cursor = con.cursor()

    sq = 'select * from task where status = "0" or status = "3"'
    cursor.execute(sq)
    for one in cursor:
        print(one[1], one[2], one[3])