import requests
import schedule
import time

phone_number = int(+254724247134)

def send_text():
    resp = requests.post('https://textbelt.com/text',{
        'phone': phone_number,
        'message': "Thank you for your contribution",
        'key' : 'textbelt'
    })
    print(resp.json())


# print(phone_number)
schedule.every(10).seconds.do(send_text)

while True:
    schedule.run_pending()
    time.sleep(1)


# look into 

# E.164 number format