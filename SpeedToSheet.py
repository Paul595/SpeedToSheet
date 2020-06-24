import gspread
from oauth2client.service_account import ServiceAccountCredentials

import speedtest
from datetime import datetime
import sys
import os
import time

spreadsheet_name = 'Raspi-SpeedTest' #change to your filename

def writeToSheet(data):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'] #specify used apis in project

    storepath = os.path.abspath(os.path.dirname(__file__))
    credentials = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(storepath, "auth.json"), scope) #create credentials for login

    gc = gspread.authorize(credentials) #authorize acces via json file

    wks = gc.open(spreadsheet_name).sheet1 #open spreadsheet for reading/writing

    wks.append_row(data) #write data into first free row in sheet


def SpeedTest():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()

    # print(res)

    return [ "", float(res["ping"]), float(humanbytes(res["download"])), float(humanbytes(res["upload"])), int(res["server"]["id"]), res["server"]["name"]+"/"+res["server"]["sponsor"], res["server"]["country"] ]




def humanbytes(B):
    'Return the given bytes as a human friendly KB, MB, GB, or TB string'
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # 1,099,511,627,776
    return '{0:.2f}'.format(B/MB)
  

def showInTerminal(data):
    print("Ping: "+str(data[2]) +"ms")
    print("Download: "+str(data[3]) +"MBps")
    print("Upload: "+str(data[4]) +"MBps")
    print("ServerID: "+str(data[5]))
    print("ServerName: "+str(data[6]))
    print("ServerCountry: "+str(data[7]))
    print("\n Use flag --silent to suppress output")


def main():
    data = SpeedTest()

    writeToSheet(data)

    if(len(sys.argv)<1):
        showInTerminal(data)


if __name__ == "__main__":
    main()