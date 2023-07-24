import requests
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass
from bs4 import BeautifulSoup

def send_email( i ):
  # create message object instance
  msg = MIMEMultipart()
  
  # the parameters of the message
  password = your_password
  msg['From'] = your_email
  msg['To'] = send_email_to
  msg['Subject'] = "Crypto Price Alert"

  # your message
  if ( i == 0 ):
    message = "Bitcoin price is now " + str(bitcoin_rate)
  elif ( i == 1 ):
    message = "Bitcoin price is up and down than 50"
  elif ( i == 2 ):
    message = "DOGE/BTC ratio is lower than 3.5e-06"

  # adds in the message from the above variable
  msg.attach(MIMEText(message, 'plain'))
  
  # create the gmail server
  server = smtplib.SMTP('smtp.gmail.com: 587')
  
  server.starttls()
  
  # Login Creds for sending the email
  server.login(msg['From'], password)
  
  # sends the message
  server.sendmail(msg['From'], msg['To'], msg.as_string())
  
  server.quit()
  
  # prints to your console
  #print("successfully sent email to %s" % (msg['To']))
  #print("Price of bitcoin was at " + str(bitcoin_rate))

# user inputs
#your_name = input('Enter your name: ')
#your_email = input('Enter your email address (gmail only): ')
#your_password = getpass.getpass()
#send_email_to = input('Enter email address to send to: ')

#https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp

your_name = "BitcoinTest"
your_email = "611410083@alum.ccu.edu.tw"
your_password = getpass.getpass("passward:")
send_email_to = "bitcointest0206@gmail.com"
#alert_amount = "23500"
temp = 0

def get_doge_price_robin(coin):
    url                 = "https://robinhood.com/crypto/"+coin
    HTML                = requests.get(url)
    soup                = BeautifulSoup(HTML.text,'html.parser')
    
    price_text          = soup.find("span",{"class":["css-15ltlny"]}).text[1:8]
    
    return float(price_text)

def get_btc_price_robin(coin):
    url                 = "https://robinhood.com/crypto/"+coin
    HTML                = requests.get(url)
    soup                = BeautifulSoup(HTML.text,'html.parser')
    
    price_text          = soup.find("span",{"class":["css-15ltlny"]}).text[1:7]
    price_text = price_text.replace(",", "")
    
    return int(price_text)

while True:
  url = "https://api.coindesk.com/v1/bpi/currentprice.json"
  response = requests.get(
    url, 
    headers={"Accept": "application/json"},
  )
  data = response.json()
  #print(data)
  
  bpi = data['bpi']
  USD = bpi['USD']
  bitcoin_rate = int(USD['rate_float'])

  #dataTime = data['time']
  #date = dataTime['updatedISO']
  localtime = time.strftime("20%y-%m-%d %H:%M", time.localtime())
  """
  if get_doge_price_robin("DOGE") / get_btc_price_robin("BTC") <= 3.4e-06:
    send_email(2)
    print( localtime, 'DOGE/BTC ratio is ' + str(round(get_doge_price_robin("DOGE") / get_btc_price_robin("BTC"), 8 ) ), "Successfully sent email" )
  elif get_doge_price_robin("DOGE") / get_btc_price_robin("BTC") > 3.6e-06:
    send_email(2)
    print( localtime, 'DOGE/BTC ratio is ' + str(round(get_doge_price_robin("DOGE") / get_btc_price_robin("BTC"), 8 ) ), "Successfully sent email" )
  else:
    print( localtime, 'DOGE/BTC ratio is ' + str(round(get_doge_price_robin("DOGE") / get_btc_price_robin("BTC"), 8 ) ) )
  """
  if abs(bitcoin_rate - temp) > 50:
    send_email(1)
    print( localtime, 'Price is ' + str(bitcoin_rate), "Successfully sent email" )
  elif bitcoin_rate > 30500:
    send_email(0)
    print( localtime, 'Price is ' + str(bitcoin_rate), "Successfully sent email" )
  elif bitcoin_rate < 29500:
    send_email(0)
    print( localtime, 'Price is ' + str(bitcoin_rate), "Successfully sent email" )
  else:
    print( localtime, 'Price is ' + str(bitcoin_rate) )

  temp = bitcoin_rate
  time.sleep(60)



















