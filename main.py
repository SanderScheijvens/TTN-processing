from modules import api, database, python_mysql_dbconfig
import time

if __name__ == "__main__":
    while True:
        data_tem, data_hum, data_time, device = api.get_data()
        print(f"temp: {data_tem}\n"
              f"hum: {data_hum}\n"
              f"time: {data_time}\n")
        time_db = database.get_time(data_time)
        if time_db != data_time:
            c = database.send_data(data_tem, data_hum, data_time, device)
        time.sleep(10)