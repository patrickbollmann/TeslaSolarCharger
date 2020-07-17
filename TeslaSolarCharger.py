import requests
import myTesla
from bs4 import BeautifulSoup
import time
teslaemail = 'your tesla email'
teslapassword = "your tesla password"
pvhost = "pv server host eg. ip like 192.168.0.xxx"
pvuser = 'pv server username'
pvpassword = 'pv server password'
charging = 0
threshold = 3000 #power threshold in watts at which charging the EV should be started

car = myTesla.connect(teslaemail, teslapassword)  #connect to vehicle using myTesla api

while True:
    try:    #try catch is used to catch server errors and connection problems
        r = requests.get(pvhost, auth=(pvuser, pvpassword)
                         )  # get piko solar webinterface
        soup = BeautifulSoup(r.text, 'html.parser')

        # find power produced at this moment in watts
        power = soup.find_all("td")[14].text.strip()
        
    except Exception as e:
        print(e)
        
    if(power == "x x x"):  # convert text to int value
        solarpower = 0
    else:
        solarpower = int(power)

    print("solar power is: "+str(solarpower)+" W")

    if (solarpower >= threshold and charging == 0):  # if enough power available start charging
        car.wake_up
        time.sleep(15) # wait for car to wake
        car.charge_start()
        charging = 1
        print("started charging")
    if (solarpower >= threshold and charging == 1):
        print("charging...")

    if (solarpower < threshold and charging == 1):  # if not enough power available stop charging
        car.wake_up
        car.charge_stop()
        charging = 0
        print("stopped charging")
    if (solarpower < threshold and charging == 0):
        print("not charging")

    time.sleep(20)  # wait 20 seconds before next power check
