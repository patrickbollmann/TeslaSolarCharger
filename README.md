# TeslaSolarCharger
Small python script to optimize your tesla electric vehicle charging process in combination with power from a solarsystem using an old PIKO/Kostal solar inverter.

Start this script after when plugging in your Tesla.
Charging your EV will automatically start if enough self produced solar power is available and stops if power is to low. This will result in an optimal usage of self produced power and saves cost during Power bought off the grid is much more expensive.

The threshold which defines "enough power to charge" is set to 3000 watts by default. Whis represents charging your Telsa at 230V single phased off a normal wall plug. If you are using a Wallbox with higher charge power you might want to change this setting.
Available power will be updated every 20 seconds, which stops charging even if a big cloud passes your area

Depending on which solar inverter you are using, you might have to change some parsing of the webinterface.

Using myTesla for communication with the Car: https://github.com/zmsp/python-my-tesla
