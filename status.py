################################################################################
## Import Libraries
from selenium import webdriver
import time
import smtplib
import argparse

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

print(f"{args['user']}")

################################################################################
## Set options for Selenium
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('window-size=1920x1080')
options.add_argument('log-level=3')

################################################################################
## Get Flag Status
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.tn.gov/about-tn/flag-status.html")

flag = driver.find_element_by_class_name("textimage-text")

status = flag.text
print(status)

driver.close()
driver.quit()

################################################################################
## Send SMS for flag status
if args['test']:
    print("testing mode -- skipping email")
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
