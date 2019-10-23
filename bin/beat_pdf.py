#!/usr/bin/python
#-*- coding:utf-8 -*-
import pdfkit
import os
import sys
import json
import datetime
import time
import random
sys.path.append('./lib/')
from xyy.GenBeatInfo import beat_info
from xyy.GenBeatInfo import beat_payment
from xyy.GenBeatInfo import beat_pdf
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font


with open('../config/beat.json') as beat_json:
	json_file=json.load(beat_json)
config = pdfkit.configuration(wkhtmltopdf=json_file['pdfkit_location'])

workbook=Workbook()
workesheet=workbook.active
workbook.title="sheet1"
font1=Font(name='dengxian')
row=1



start_day=json_file['start_date']
end_day=json_file['end_date']
d1=datetime.datetime(int(start_day[0:4]),int(start_day[4:6]),int(start_day[6:]))
d2=datetime.datetime(int(end_day[0:4]),int(end_day[4:6]),int(end_day[6:]))
interval_1=d2-d1
for i in range(1,int(interval_1.days)):
    payment_amount=beat_payment().payment_format(json_file['start_amt'],json_file['interval'])
    name=beat_info().dirver_name()
    car=beat_info().car()
    car_no=beat_info().drive_license()
    timeStruct1 = time.strptime(json_file['start_date']+' '+json_file['go_time'], "%Y%m%d %H:%M")
    timeStamp1=time.mktime(timeStruct1)
    if random.randint(0,1)==1:
        timeStamp1+=random.randint(0,json_file['interval_min'])*60
    else:
        timeStamp1+=random.randint(0,json_file['interval_min'])*-60
    timeStamp1+=24*3600*(i-1)
    curr_time1= time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(timeStamp1))
    curr_time_file=time.strftime("%Y.%m.%d", time.localtime(timeStamp1))
    week=time.localtime(timeStamp1)[6]
    print(week)
    if json_file['skip_weekend']==True and (week==6 or week==5):
        continue
    else:
        beat_pdf().create_html_file(json_file['start_address'],json_file['end_address'],payment_amount,curr_time1,name,car,car_no)
        pdfkit.from_file('../output/temp.html','../output/'+curr_time_file+'.pdf',configuration=config)
        workesheet['A'+str(row)]=curr_time_file
        workesheet['B'+str(row)]=payment_amount
        workesheet['C'+str(row)]='Beat打车'
        row+=1
    if json_file['round_trip'] == True:
        payment_amount=beat_payment().payment_format(json_file['back_amt'],json_file['interval'])
        name=beat_info().dirver_name()
        car=beat_info().car()
        car_no=beat_info().drive_license()
        timeStruct2 = time.strptime(json_file['start_date']+' '+json_file['back_time'], "%Y%m%d %H:%M")
        timeStamp2=time.mktime(timeStruct2)
        if random.randint(0,1)==1:
            timeStamp2+=random.randint(0,json_file['interval_min'])*60
        else:
            timeStamp2+=random.randint(0,json_file['interval_min'])*-60
        timeStamp2+=24*3600*(i-1)
        curr_time2= time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(timeStamp2))
        print(curr_time2)
        curr_time_file2=time.strftime("%Y.%m.%d", time.localtime(timeStamp1))
        if json_file['skip_weekend']==True and (week==6 or week==5):
            continue
        else:
            beat_pdf().create_html_file(json_file['end_address'],json_file['start_address'],payment_amount,curr_time2,name,car,car_no)
            pdfkit.from_file('../output/temp.html','../output/'+curr_time_file2+'(2).pdf',configuration=config)
            workesheet['A'+str(row)]=curr_time_file
            workesheet['B'+str(row)]=payment_amount
            workesheet['C'+str(row)]='Beat打车'
            row+=1
        #if(random.random(0,1))==1:
workbook.save('../output/taxi_detail.xlsx')
os.remove('../output/temp.html')


#file=open('tep.html','w')
#file.write(html_content)
#file.close()
#
#pdfkit.from_file('./tep.html', 'tep.pdf',configuration=config)
#os.remove('tep.html')
#print(beat_payment().payment_format(100000,10))

