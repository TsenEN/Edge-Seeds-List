import mysql.connector
from mysql.connector import Error
try:
    # 連接 MySQL/MariaDB 資料庫
    connection = mysql.connector.connect(
        host='localhost',          # 主機名稱
        database='smartdb', # 資料庫名稱
        user='Tsen',        # 帳號
        password='CTsen')  # 密碼

    if connection.is_connected():

        # 顯示資料庫版本
        db_Info = connection.get_server_info()
        print("資料庫版本：", db_Info)

        # 顯示目前使用的資料庫
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("目前使用的資料庫：", record)

    cursor = connection.cursor()

    #Creating table as per requirement
    sql ='''CREATE TABLE seed(
        seed_id INT NOT NULL,
        seed_x DOUBLE ,
        seed_y DOUBLE ,
        seed_z DOUBLE ,
        seed_battery DOUBLE ,
        seed_status INT,
        seed_latitude DECIMAL(10,7) NOT NULL,
        seed_longitude DECIMAL(10,7) NOT NULL,
        PRIMARY KEY(seed_id)
    );'''
    cursor.execute(sql)

    #Closing the connection
    connection.close()

except Error as e:
    print("資料庫連接失敗：", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("資料庫連線已關閉")