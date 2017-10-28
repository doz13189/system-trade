import requests

def get_market_api():
	#エンドポイントURL
	endpoint = "https://api.bitflyer.jp"

	#欲しい情報
	path = "/v1/getmarkets"

	#完成するURL
	print(endpoint + path)

	#リクエストを送って、レスポンスを受け取っている
	response = requests.get(endpoint + path)
	print(response)
	
	#読める形にする
	response = response.text

	return response

response = get_market_api()
print(response)