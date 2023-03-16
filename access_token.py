from fyers_api import accessToken
from fyers_api import fyersModel
from selenium import webdriver
import sys
import time
import re

driver=webdriver.Chrome()

app_id = ""

app_secret = ""

app_session = accessToken.SessionModel(app_id, app_secret)

response = app_session.auth()


auth_code=response["data"]["authorization_code"]
print(auth_code)

app_session.set_token(auth_code)

generate_url=app_session.generate_token()

print(generate_url)

driver.get(generate_url)

user_name = driver.find_element_by_id('fyers_id')
password = driver.find_element_by_id('password')
pan_card = driver.find_element_by_id('pancard')
submit_button = driver.find_element_by_id('btn_id')
# Fill in the credentials
user_name.send_keys('')
password.send_keys('')
pan_card.send_keys('')
time.sleep(1)
submit_button.click()
time.sleep(5)
url_with_token = driver.current_url


# access_token_generated = re.search(r'(?<=http://localhost:3000/?access_token=).*?(?=user_id=XR00275)', url_with_token).group(0)

print(url_with_token)