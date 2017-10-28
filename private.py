import requests
import json
import time
import hmac
import hashlib


#資産残高を取得	
def get_balance_api():

	#API keyとAPI secret
	api_key = "***********************"
	api_secret = b"**************************************"	

	#エンドポイントURL
	endpoint = "https://api.bitflyer.jp"

	#認証情報の作成
	method = "GET"
	path = "/v1/me/getbalance"
	timestamp = str(time.time())

	text = timestamp + method + path

	sign = hmac.new(api_secret, text.encode('utf-8'), hashlib.sha256).hexdigest()


	#ヘッダーの情報
	headers = {
		'ACCESS-KEY': api_key,
		'ACCESS-TIMESTAMP': timestamp,
		'ACCESS-SIGN': sign,
		'Content-Type': 'application/json'
	}

	#リクエストを送って、レスポンスを受け取る
	response = requests.get(endpoint + path, headers=headers)
	print(response)

	response = response.text

	return response

response = get_balance_api()
print(response)