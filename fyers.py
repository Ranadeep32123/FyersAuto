from fyers_api import accessToken

from fyers_api import fyersModel

'''app_id = "RAEKVHXTSR"

app_secret = "DX46K5D53E"

app_session = accessToken.SessionModel(app_id, app_secret)

response = app_session.auth()

print(response)
'''
'''
authorization_code = “eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqaGdqZzg3NiQ3ODVidjVANjQ3NTZ2NSZnNyM2OTg3Njc5OHhkIjoiUkFFS1ZIWFRTUiIsImV4cCI6MTYxMjYwMTM5MS45MTcyfQ.5q9ReqqacMYo21zDZZjEKKgXGWpO5viMFtGOWcBjqzw”

app_session.set_token(authorization_code)

app_session.generate_token()'''


token="gAAAAABf6uVZSNziJ7Ri7mAQ9PFKfaMwYnFqiQKJj50khaUA366UQbpDx3T_DfPmEuzA94OYtNcoKj7ClzwR_kD81mD_Mt5kWSpXvMEunEoeWDadozQxi_o="

is_async = False #(By default False, Change to True for asnyc API calls.)

fyers = fyersModel.FyersModel(is_async)

print(fyers. get_profile(token = token))

print(fyers.place_orders(
token = token,
data = {
"symbol" : "NSE:NIFTY20DEC14100CE",
"qty" : 750,
"type" : 2,
"side" : -1,
"productType" : "INTRADAY",
"limitPrice" : 0,
"stopPrice" : 0,
"disclosedQty" : 0,
"validity" : "DAY",
"offlineOrder" : "False",
"stopLoss" : 0,
"takeProfit" : 0
}
))

print(fyers.place_orders(
token = token,
data = {
"symbol" : "NSE:NIFTY20DEC13700PE",
"qty" : 750,
"type" : 2,
"side" : -1,
"productType" : "INTRADAY",
"limitPrice" : 0,
"stopPrice" : 0,
"disclosedQty" : 0,
"validity" : "DAY",
"offlineOrder" : "False",
"stopLoss" : 0,
"takeProfit" : 0
}
))



