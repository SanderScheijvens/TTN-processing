from mysql.connector import MySQLConnection, Error
from modules.python_mysql_dbconfig import read_db_config


def send_data(data_tem, data_hum, data_time, device):
    db_config = read_db_config()
    conn = None
    try:
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')

    except Error as error:
        print(error)


    finally:
        if conn is not None and conn.is_connected():
            cursor = conn.cursor()

            val = (data_time, data_tem, data_hum, device)
            sql = "INSERT INTO data (data_time, data_tem, data_hum, data_device) VALUES (%s, %s, %s, %s)"

            cursor.execute(sql, val)
            conn.commit()
            conn.close()

def get_time(time_API):
    db_config = read_db_config()
    conn = None
    try:
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')

    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            cursor = conn.cursor()

            val = (time_API,)
            sql = "SELECT data_time FROM data WHERE data_time = %s"

            cursor.execute(sql, val)
            result = cursor.fetchall()
            conn.close()
            if not result:
                result1 = ''
                return result1
            else:
                result_time = result[0]
                return result_time[0]

