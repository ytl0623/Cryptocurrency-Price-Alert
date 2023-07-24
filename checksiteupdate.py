import os
import hashlib
import urllib.request
import json
import codecs
import ssl

import requests
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass

def checksiteupdate() :
    ssl._create_default_https_context = ssl._create_unverified_context


    #輸入想要追蹤的網址，可以增加或刪除
    site=['https://career.ccu.edu.tw/p/412-1038-285.php?Lang=zh-tw',
         
         ]


    #檢查json檔案是否存在，若沒有則建立一個
    try:
        my_file = open('sitechange.json')
    except IOError:
        data={}
        with open('sitechange.json','w') as outfile:
            json.dump(data, outfile, ensure_ascii=False)

        
    #開啟json檔案，讀入資料
    with open("sitechange.json") as infile:
        data = infile.read()
        local_data = json.loads(data)

    #檢查json檔中是否有相關網址紀錄，若沒有則建立一個
    for i in range(len(site)):
        if site[i] not in local_data:
            local_data[site[i]]=""

    #若用戶刪除網址紀錄，則更新json檔
    temp=local_data.copy()
    for i in local_data.keys():
        if i not in site:
            temp.pop(i)

    local_data=temp


    #讀入相關網址，並找出其雜湊值，與已儲存的雜湊值進行對比
    for i in range(len(site)):
        remote_data = urllib.request.urlopen(site[i]).read()
        remote_hash = hashlib.md5(remote_data).hexdigest()

        if remote_hash == local_data[site[i]]:
            print(localtime, site[i]+' has no update')
        else:
            send_email(site[i])
            print(localtime, site[i]+' is modified')
            local_data[site[i]]=remote_hash

    #把更新的雜湊值寫回json檔
    with open('sitechange.json','w') as outfile:
        json.dump(local_data, outfile, ensure_ascii=False)

def send_email(site):
  # create message object instance
  msg = MIMEMultipart()
  
  # the parameters of the message
  password = your_password
  msg['From'] = your_email
  msg['To'] = send_email_to
  msg['Subject'] = "Check Site Update"

  # your message
  message = "The website has been update.\n\nPlease check the following url: "
  html = site

  # adds in the message from the above variable
  msg.attach(MIMEText(message, 'plain'))
  msg.attach(MIMEText(html, 'html'))
  
  # create the gmail server
  server = smtplib.SMTP('smtp.gmail.com: 587')
  
  server.starttls()
  
  # Login Creds for sending the email
  server.login(msg['From'], password)
  
  # sends the message
  server.sendmail(msg['From'], msg['To'], msg.as_string())
  
  server.quit()

your_name = "BitcoinTest"
your_email = "611410083@alum.ccu.edu.tw"
your_password = "bitcointest0206??"
send_email_to = "bitcointest0206@gmail.com"

while True:
    localtime = time.strftime("20%y-%m-%d %H:%M", time.localtime())
    checksiteupdate()
    time.sleep(3600)




















