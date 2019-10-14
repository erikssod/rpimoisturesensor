# rpi zero moisture sensor et al

## tl;dr
An underhanded attempt to involve other, gifted, people in my automated garden efforts. Because holy shirtballs these tiny, wifi-enabled raspberry zero's are the bees knees! 

## ProofOfPrinciple.py
Reads out from three moisture sensors. These are powered from a GPIO pin, and only briefly energised when reading out.

|RPi Zero|Sensor|Other bit|
|:-------------:|:-------------:|:-------------:|
|![alt text][tiny]|![alt text][stab]|![alt text][pot]|
|Full size USB for scale|So cheap|Thresholding pot|

[tiny]: https://github.com/erikssod/rpimoisturesensor/blob/master/images/IMG_20191013_122024.jpg "Tiny!"
[stab]: https://github.com/erikssod/rpimoisturesensor/blob/master/images/IMG_20191006_173445.jpg "Stab!"
[pot]: https://github.com/erikssod/rpimoisturesensor/blob/master/images/IMG_20191006_173437.jpg "Pot!"

Current sensors in use are the [resistive variant](https://www.auselectronicsdirect.com.au/soil-moisture-sensor-module-for-arduino-projects), which are dirt cheap ($1.50), but supposedly don't last very long. Doesn't matter much as long as they can be easily swapped out. In the current confuguration, they only read out above or below threshold (i.e. DRY or WET). This threshold can be tuned via individual pots.

Next generation sensors are [capacitive](https://thepihut.com/products/gravity-analog-capacitive-soil-moisture-sensor-corrosion-resistant). These are more expensive ($15.00), but supposed to be far more durable. Also, supposed to be easier to configure for analogue readout (i.e wetness level on a scale).

## Single-board computer
RPi zero WH (Wireless with soldered Headers on the 40x GPIO). Current plan is to run one per garden bed (i.e. four). I have five already. They appear to consume very little power, and can proably be fed from a battery pack that recharges over day from a cheap solar cell. I ran an RPi powering a string of fairy lights, and reponding to pings, for twelve hours on a 8Wh (3.7V, 2200mAh) battery.

## OS (proposed)
Currently Raspbian light, but open for suggestions. I've looked into Alpine and Arch, and there are communities for both. Since there is likely to be up to four devices, some kind of orchestration is planned. Either Salt, or some way to run docker images comes to mind. 

Ordered 5 x 2Gb micro SD cards on the cheap with the intention that the OS should be kept lean. Could be upped if this is an issue. 

## Backend (proposed)
...Python? Python. The RPi.GPIO library seems to have good support for writing testbeds that can be used as simulated inputs for the readout code. Means all development can happen outside the RPi's themselves. 

YAML config files seems like a thing to have to abstract out which physical pins get used in the code proper. Ideally, one config file for the whole project and not one per RPi. Individual RPi's can be identified based on e.g. mac address or so. 

Process control via e.g. systemcl or supervisor. Because that's what I know, not because it's best. See above docker comment if applicable. 

## Database (proposed)
*\*Points vaguely at the sky\**. Gotta use that wifi connectivity, and my Google Drive account.

## Frontend (proposed)
Mostly data plotting for now. Local webpage with live readout sounds about right. Future projects (e.g. RPi powered solenoids for a watering system!) will require inputs as well as readouts. 
