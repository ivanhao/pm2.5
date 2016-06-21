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
#---------email---------------#
sender = 'youremail@qq.com'   #need to change
to_list = [ 'aaa@qq.com', 'bbb@qq.com' ]  #need to change
subject = 'PM2.5:'+ aqi + '--' + level  #optinal to change
smtpserver = 'smtp.qq.com'  #smtp url optional to change
username = 'your sender email username'  #need to change
password = 'email password'  #need to change

msg = MIMEText('<td>PM2.5: '+aqi+'</td><br><td>状态：'+level+'</td><br><td>更新时间: '+time+'</td>', 'html')  #optional to change
msg['Subject'] = subject  
smtp = smtplib.SMTP()  
smtp.connect(smtpserver)  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string()) 
smtp.quit()  
