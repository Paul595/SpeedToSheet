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
To get an Autheication Key for your Google Spreadsheet please use this Youtube Video (To be added)

After you have got your json file rename it to "auth.json" and add it to the directory of SpeedToSheet.py

## Setup Complete
