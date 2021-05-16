# Covid Vaccine Slot Finder

![](https://forthebadge.com/images/badges/made-with-python.svg)

## Description
A simple python script to get the alert on vaccine slot availablity on a particular PIN code in India. Upon finding the slots in your area, ```warning.mp3``` will be played to get your attention so that you can book the appointments.

## Prerequisites
The Code is written in Python 3.8. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. 

To install pip run in the command Line
```
python -m ensurepip -- default-pip 
``` 
to upgrade it
```
python -m pip install -- upgrade pip setuptools wheel
```
to upgrade Python
```
pip install python -- upgrade
```
**Important**
Shoot this command to install additional required packages:
```
pip install -r requirements.txt
```

## Run Script
Open Terminal or Command Prompt and type
```
python individual_vaccine_slot_finder.py -p 125053
```
Running this script will continuously check for available slot in the PIN code 125053.

### Required Argument
  **-p PINCODE, --pincode PINCODE** 
 - PIN Code to look for vaccination slots.

### Optional Arguments
  **-h, --help**
- show this help message and exit
  
 **-a [18,45], --minAge [18,45]**
- Minimum age to find the slots for. Default is 18.

 **-d DATE, --date DATE** 
-  Date on which you want to find the slots. Format - '16-05-2021'

## Does this even work?
Getting an appointment for vaccination is a huge challenging in my area. I have been able get the vaccination with my entire family just because of the script. I am using a scalable version of the same script to get the slots availability alert for my near and dear ones. So yes, it works at the time of latest commit.

## Found it useful?
Please book the appointment for one who doesn't have the access to internet. They need it the most.

## Troubleshooting
The [www.cowin.gov.in](https://www.cowin.gov.in)'s server will block your request after some time if you continue to send request using the same IP address. To tackle it, some free proxies from ```proxies.py``` are randomaly being rotated in a random time interval. Feel free to add some more **https** proxies to keep the script running.

## Team
[![Rohit Swami](https://avatars1.githubusercontent.com/u/16516296?v=3&s=144)](https://rohitswami.com/) |
-|
[Rohit Swami](https://rohitswami.com/) |)

## License
[![Apache license](https://img.shields.io/badge/license-apache-blue?style=for-the-badge&logo=appveyor)](http://www.apache.org/licenses/LICENSE-2.0e)

Copyright 2021 Rohit Swami

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
