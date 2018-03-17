################################################################################
## Import Libraries
import smtplib
import argparse
import requests
from bs4 import BeautifulSoup as bs
import configparser

config = configparser.ConfigParser()
config.read("./status.ini")
current = config['status']['current']

################################################################################
## Args for sending email (sms)
ap = argparse.ArgumentParser(description='SMS updates for TN flag status')
ap.add_argument("-u", "--user", required=True, help="User name")
ap.add_argument("-p", "--password", required=True, help="Password")
ap.add_argument("-s", "--server", required=True, help="SMTP server")
ap.add_argument("--port", default=587, help="SMTP port")
ap.add_argument("-f", "--from", required=True, help="FROM email address")
ap.add_argument("-t", "--to", required=True, help="TO eamil address")
ap.add_argument("--test", default=False, help="for travis ci (skips sending email)")
args = vars(ap.parse_args())

################################################################################
## Set options for Selenium
p = requests.get("https://www.tn.gov/about-tn/flag-status.html")

s = bs(p.content, 'html.parser')

status = list(s.find('div', class_='textimage-text').children)[1].text

################################################################################
## Send SMS for flag status
if args['test']:
    print("testing mode -- skipping email")
elif current == status:
    print("no update")
else:
    server = smtplib.SMTP(args["server"], args["port"])
    server.starttls()

    server.login(args["user"], args["password"])

    message = f"From: <{args['from']}>\n"
    message = message + f"To: <{args['to']}>\n"
    message = message + "Subject: TN Flag Status\n"
    message = message + "\n"
    message = message + f"{status.split(':')[1]}"

    server.sendmail(args["from"], args["to"], message)

    configf = open("./status.ini",'w')
    config.set('status','current', status)
    config.write(configf)
    configf.close()
