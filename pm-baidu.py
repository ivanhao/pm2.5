#!/bin/python
# -*- coding: utf-8 -*-
import smtplib  
from email.mime.text import MIMEText  
import urllib, urllib2, json
#-------Get PM2.5-----------#
url = 'http://apis.baidu.com/apistore/aqiservice/aqi?city=%E5%8C%97%E4%BA%AC' #need to change city code,current is beijing
req = urllib2.Request(url)

req.add_header("apikey", "your baidu api key")  #need to change

resp = urllib2.urlopen(req)
content = resp.read()
content = json.loads(content)

if(content):
    pm = content['retData']
    level = str(pm['level'].encode("utf-8"))
    aqi = str(pm['aqi'])
    time = str(pm['time']) 
    city = str(pm['city'].encode("utf-8"))
#---------Get Weather---------#
url = 'http://apis.baidu.com/apistore/weatherservice/weather?citypinyin=beijing'

req = urllib2.Request(url)

req.add_header("apikey", "3a07c303a126715c43364484692fbed5")

resp = urllib2.urlopen(req)
content = resp.read()
content = json.loads(content)
if(content):
    w = content['retData']
    wtime = str(w['time'])
    weather = str(w['weather'].encode("utf-8"))
    temp = str(w['temp'].encode("utf-8"))
    ws = str(w['WS'].encode("utf-8"))
#---------email---------------#
sender = 'youremail@qq.com'   #need to change
to_list = [ 'aaa@qq.com', 'bbb@qq.com' ]  #need to change
subject = 'PM2.5：'+ aqi + '--' + level + '   天气：' + weather + '--' + temp + '度'  #optional to change
smtpserver = 'smtp.qq.com'  #smtp url optional to change
username = 'your sender email username'  #need to change
password = 'email password'  #need to change

msg = MIMEText('<td>城市(city): '+city+'</td><br><td>PM2.5: '+aqi+'</td><br><td>状态(status)：'+level+'</td><br><td>更新时间(last update): '+time+'</td><br><br><td>天气：'+weather+'</td><br><td>气温：'+ temp + '</td><br><td>风力：' + ws + '</td><br><td>更新时间：'+ wtime + '</td>', 'html')
msg['Subject'] = subject  
smtp = smtplib.SMTP()  
smtp.connect(smtpserver)  
smtp.login(username, password)  
smtp.sendmail(sender, to_list, msg.as_string()) 
smtp.quit()  
