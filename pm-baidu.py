#!/bin/python
# -*- coding: utf-8 -*-
import smtplib  
from email.mime.text import MIMEText  
import urllib, urllib2, json
#-------Get PM2.5-----------#
url = 'http://apis.baidu.com/heweather/weather/free?city=beijing' #need to change your city
req = urllib2.Request(url)

req.add_header("apikey", "YOUR API KEY") #need to change your key

resp = urllib2.urlopen(req)
content = resp.read()
content = json.loads(content)

if(content):
    pm = content['HeWeather data service 3.0'][0]
    level = str(pm['aqi']['city']['qlty'].encode("utf-8"))
    aqi = str(pm['aqi']['city']['aqi'])
    time = str(pm['basic']['update']['loc'])
    city = str(pm['basic']['city'].encode("utf-8"))
    weather = str(pm['now']['cond']['txt'].encode("utf-8"))
    temp = str(pm['now']['tmp'])
    humi = str(pm['now']['hum'])
    ws = str(pm['now']['wind']['dir'].encode("utf-8")) + " " + str(pm['now']['wind']['sc'].encode("utf-8"))

#---------email---------------#
sender = 'youremail@qq.com'   #need to change
to_list = [ 'aaa@qq.com', 'bbb@qq.com' ]  #need to change
subject = 'PM2.5：'+ aqi + '--' + level + '   天气：' + weather + ': ' + temp + '度'  #optional to change
smtpserver = 'smtp.qq.com'  #smtp url optional to change
username = 'your sender email username'  #need to change
password = 'email password'  #need to change

msg = MIMEText('<td>城市(city): '+city+'</td><br><td>PM2.5: '+aqi+'</td><br><td>状态(status)：'+level+'</td><br><td>更新时间(last update): '+time+'</td><br><br><td>天气：'+weather+'</td><br><td>气温：'+ temp + '</td><br><td>风力：' + ws + '</td><br><td>更新时间：'+ wtime + '</td>', 'html')
msg = MIMEText('<td>城市(city): '+city+'</td><br><td>PM2.5: '+aqi+'</td><br><td>状态(status)：'+level+'</td><br><br><td>天气：'+weather+'</td><br><td>气温：'+ temp + '</td><br><td>湿度：'+humi+'</td><br>$


msg['Subject'] = subject  
smtp = smtplib.SMTP()  
smtp.connect(smtpserver)  
smtp.login(username, password)  
smtp.sendmail(sender, to_list, msg.as_string()) 
smtp.quit()  
