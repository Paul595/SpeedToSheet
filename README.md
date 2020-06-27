# SpeedToSheet
Python Script that tests your Internet Speed and uploads it to a Google Sheet

## Installation

Use the package manager pip to install the required packages
```bash
pip install gspread oauth2client speedtest-cli
```

You also have to change the name from 'Raspi-SpeedTest' to your own name
```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import speedtest
from datetime import datetime
import sys
import os

spreadsheet_name = 'Raspi-SpeedTest' #change to your filename
```


### Get Authentication for Google Spreadsheet 
To get an Autheication Key for your Google Spreadsheet please use this [Youtube Video by Pretty Printed](https://www.youtube.com/watch?v=7I2s81TsCnc)

After you have got your json file rename it to "auth.json" and add it to the directory of SpeedToSheet.py

#
You can also upload this script to a **RaspberryPi** so it can run all day and night via a cronjob

### Google Sheets Template
[Template-Raspi-SpeedTest_v1.0](https://docs.google.com/spreadsheets/d/1KqsqZV0wOWPVHPCU-lG9nBpkmcP2iwgMbTjlej6Hv2I/edit?usp=sharing) Link to a copy of my Google Sheet to view the data with graphs for the network data

Just copy it to your drive and use the scritp somewhere and you are ready!

## Setup Complete

If you have any questions feel free to contact me
