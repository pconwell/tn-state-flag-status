## Import Libraries
from selenium import webdriver

## Set options for Selenium
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('window-size=1920x1080')
options.add_argument('log-level=3')

## Selenium
driver = webdriver.Chrome(chrome_options=options)

## Open Webpage
driver.get("https://www.tn.gov/about-tn/flag-status.html")

## Get Current Flag Status
#flag = driver.find_element_by_tag_name("h3")
flag = driver.find_element_by_class_name("textimage-text")
## Output Flag Status

print(flag.text)

## Close everything
driver.close()
driver.quit()

## Wait until user exits
input("Press enter to exit...")
