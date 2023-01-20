#scrip checks every minute where ISS is right now and if it's in the target region and it's after sunset, sends an email

import requests
from datetime import datetime
import smtplib
import time
import os

# target location
LATITUDE = 50.097669
LONGITUDE = -14.430257

# target email
my_email = os.environ.get("MAIL_USERNAME")
password = os.environ.get("MAIL_PASSWORD")


def time_ok():
    # checking when there is sunrise and sunset in current location and weather now is dark
    parameters = { "lat":LATITUDE, "lng": LONGITUDE, "formatted" : 0 }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    # print(response.url)
    response.raise_for_status()
    data = response.json()
    # print(data["results"])
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(":")[0])

    now = datetime.now()
    hour= now.hour
    print(f"Sunrise: {sunrise},Sunset: {sunset}, Hour: {hour}")
    if hour > sunset:
        return True
    else:
        False


def check_iss():
    #checking where is iss flying now and if it close enough to current position
    iss = requests.get(url='http://api.open-notify.org/iss-now.json')
    position = iss.json()['iss_position']
    print(position)
    diff_lat = abs(abs(LATITUDE) - abs(float(position["latitude"])))
    diff_lng = abs(abs(LONGITUDE) - abs(float(position["longitude"])))
    print(diff_lng, diff_lat)
    if diff_lng < 5 and diff_lat < 5:
        return True

def send_mail():
    if time_ok() and check_iss():
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(password=password, user=my_email)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Look up \n\n ISS is right above you!")
            print("message was sent")
    else:
        print("message was not sent")


while True:
    send_mail()
    time.sleep(60)
