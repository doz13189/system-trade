import requests
import json
import time
import hmac
import hashlib


#取引を行うAPI
def trade_api(product_code, child_order_type, side, size):

	#API keyとAPI secret
	api_key = "***************"
	api_secret = b"******************************"

	#エンドポイントURL
	endpoint = "https://api.bitflyer.jp"

	#認証情報の作成
	method = "POST"
	path = "/v1/me/sendchildorder"
	timestamp = str(time.time())
	
	#パラメータ情報
	payload = {
		"product_code": product_code,
		"child_order_type" : child_order_type,
		"side" : side,
		"size" : size
	}

	text = timestamp + method + path + str(json.dumps(payload))
	sign = hmac.new(api_secret, text.encode('utf-8'), hashlib.sha256).hexdigest()


	#ヘッダーの情報
	headers = {
		"ACCESS-KEY": api_key,
		"ACCESS-TIMESTAMP": timestamp,
		"ACCESS-SIGN": sign,
		"Content-Type": "application/json"
	}

	response = requests.post(endpoint + path, data=json.dumps(payload), headers=headers)
	response = response.text

	return response


def get_position_api():
	#API keyとAPI secret
	api_key = "***************"
	api_secret = b"******************************"

	#エンドポイントURL
	endpoint = "https://api.bitflyer.jp"

	#認証情報の作成
	method = "GET"
	path = "/v1/me/getpositions?product_code=FX_BTC_JPY"
	timestamp = str(time.time())

	#認証情報の作成
	text = timestamp + method + path
	sign = hmac.new(api_secret, text.encode('utf-8'), hashlib.sha256).hexdigest()

	#ヘッダーの情報
	headers = {
		"ACCESS-KEY": api_key,
		"ACCESS-TIMESTAMP": timestamp,
		"ACCESS-SIGN": sign,
		"Content-Type": "application/json"
	}

	#レスポンスを受け取る
	response = requests.get(endpoint + path, headers=headers)

	#jsonファイルを保存します
	saveFile("getpositions", response.text)

	return response


def saveFile(file_name, response):
	f = open(file_name + ".json", "w")
	f.write(response)
	f.close()


def readJson(file_name):
	json_file = open(file_name + ".json", "r")
	json_file = json.load(json_file)

	return json_file


#取引を行う
def trade():
	#パラメータに付与する情報をリスト形式に
	product_code = ["BTC_JPY", "ETH_BTC", "FX_BTC_JPY"]
	child_order_type = ["LIMIT", "MARKET"]
	side = ["BUY", "SELL"]
	#priceは指し値注文（LIMIT）にした場合のみ必須
	price = []
	response = trade_api(product_code[2], child_order_type[1], side[0], 0.01)

	return response


#決済を行う
def settlement():
	#建玉を取得
	get_position_api()

	#建玉のjsonを読み込む
	position_btc = readJson("getpositions")
	print(position_btc)

	i = 1
	while True:
		try:
			# print(position_btc[i]["pnl"])
			print(position_btc[i])
		
		except IndexError:
			break
		i += 1

	# # 決済
	# i = 1
	# while True:
	# 	try:
	# 		print(position_btc[i]["size"])
	# 		trade_api(position_btc[i]["product_code"], "MARKET", "SELL", position_btc[i]["size"])
	# 	except IndexError:
	# 		break
	# 	i += 1


if __name__ == '__main__':
	#パラメータに付与する情報をリスト形式に
	product_code = ["BTC_JPY", "ETH_BTC", "FX_BTC_JPY"]
	child_order_type = ["LIMIT", "MARKET"]
	side = ["BUY", "SELL"]
	#priceは指し値注文（LIMIT）にした場合のみ必須
	price = []

	# response = trade_api(product_code[2], child_order_type[1], side[1], 0.01)
	# print(response)

	response = trade()
	print(response)

	response = get_position_api()
	print(response)

	settlement()
