import requests, json

def get_data():
    myUrl = 'https://lora-test-node-beegden.data.thethingsnetwork.org/api/v2/query?last=1d'
    headers = {
        'Accept': 'application/json',
        'Authorization': 'key ttn-account-v2.zZlBorjL4MZNSSDe4Hjhjq8raa_5oyLpZw4eXMRxEr8'
    }
    r = requests.get(myUrl, headers=headers)
    if r.ok:
        data = r.json()
        data = data[-1]
        data_hum = data['humidity']
        data_tem = data['degreesC']
        data_time = data['time']
        device = data['device_id']
        if int(data_tem) >= 99 and int(data_hum) >= 99:
            data_tem = None
            data_hum = None
        else:
            data_tem = round(data_tem, 2)
            data_hum = round(data_hum, 2)
        return data_tem, data_hum, data_time, device
    else:
        print('ERROR')