import requests
import json
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass
from bs4 import BeautifulSoup

def get_price():
    doge = requests.get( "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT" )
    dump = json.loads( doge.content )
    price = float( dump['price'].strip( "0" ) )
    return price

def send_email( price, i ):
    # create message object instance
    msg = MIMEMultipart()

    # the parameters of the message
    password = your_password
    msg['From'] = your_email
    msg['To'] = send_email_to
    msg['Subject'] = "BTC/USDT Price Alert"

    # your message
    if ( i == 0 ):
        message = "BTC/USDT price is now " + str( price )
    elif ( i == 1 ):
        message = "BTC/USDT price is up and down than 50"

    # adds in the message from the above variable
    msg.attach(MIMEText( message, "plain" ) )

    # create the gmail server
    server = smtplib.SMTP( "smtp.gmail.com: 587" )

    server.starttls()

    # Login Creds for sending the email
    server.login( msg['From'], password )

    # sends the message
    server.sendmail( msg['From'], msg['To'], msg.as_string() )

    server.quit()

your_email = "611410083@alum.ccu.edu.tw"
your_password = getpass.getpass( "passward:" )
send_email_to = "bitcointest0206@gmail.com"
temp = 0

while True:
    localtime = time.strftime( "20%y-%m-%d %H:%M", time.localtime() )

    price = get_price()

    if abs( price - temp ) > 50:
        send_email( price, 1 )
        print( localtime, "Price is " + str( price ), "Successfully sent email" )
    elif ( price ) >= 30000:
        send_email( price, 0 )
        print( localtime, "Price is " + str( price ), "Successfully sent email" )
    elif ( price ) < 28000:
        send_email( price, 0 )
        print( localtime, "Price is " + str( price ), "Successfully sent email" )
    else:
        print( localtime, 'Price is ' + str( price ) )

    temp = price
    time.sleep( 60 )

















