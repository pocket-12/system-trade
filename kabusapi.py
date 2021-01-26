'''
auカブコムSPIモジュール
'''
#必要なモジュールをインストール
import urllib.request
import json
import pprint
'''
１．トークン発行 コマンド
※１で発行したtokenを２以降の各ファイル内の「X-API-KEY」に指定する
'''
#kabusapi_token.py 

obj = { 'APIPassword': 'qwerty' }
json_data = json.dumps(obj).encode('utf8')

url = 'http://localhost:18080/kabusapi/token'
req = urllib.request.Request(url, json_data, method='POST')
req.add_header('Content-Type', 'application/json')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
２．注文発注（現物）
'''
#（１）買 コマンド:python kabusapi_sendorder_cash_buy.py

obj = { 'Password': '123456',
        'Symbol': '9433',
        'Exchange': 1,
        'SecurityType': 1,
        'FrontOrderType': 20,
        'Side': '2',
        'CashMargin': 1,
        'DelivType': 2,
        'FundType': 'AA',
        'AccountType': 2,
        'Qty': 100,
        'Price': 2762.5,
        'ExpireDay': 20200924 }
json_data = json.dumps(obj).encode('utf-8')

url = 'http://localhost:18080/kabusapi/sendorder'
req = urllib.request.Request(url, json_data, method='POST')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

#（２）売 コマンド:python kabusapi_sendorder_cash_sell.py
obj = { 'Password': '123456',
        'Symbol': '9433',
        'Exchange': 1,
        'SecurityType': 1,
        'FrontOrderType': 20,
        'Side': '1',
        'CashMargin': 1,
        'DelivType': 0,
        'FundType': '  ',
        'AccountType': 2,
        'Qty': 100,
        'Price': 2762.5,
        'ExpireDay': 20200924 }
json_data = json.dumps(obj).encode('utf-8')

url = 'http://localhost:18080/kabusapi/sendorder'
req = urllib.request.Request(url, json_data, method='POST')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
３．注文発注（信用）
'''
#新規 コマンド：python kabusapi_sendorder_margin_new.py
obj = { 'Password': '123456',
        'Symbol': '9433',
        'Exchange': 1,
        'SecurityType': 1,
        'FrontOrderType': 20,
        'Side': '2',
        'CashMargin': 2,
        'MarginTradeType': 2,
        'DelivType': 0,
        'AccountType': 2,
        'Qty': 100,
        'Price': 2762.5,
        'ExpireDay': 20200924 }
json_data = json.dumps(obj).encode('utf-8')

url = 'http://localhost:18080/kabusapi/sendorder'
req = urllib.request.Request(url, json_data, method='POST')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)
#返済（決済順序） コマンド：python kabusapi_sendorder_margin_pay_ClosePositionOrder.py

obj = { 'Password': '123456',
        'Symbol': '9433',
        'Exchange': 1,
        'SecurityType': 1,
        'FrontOrderType': 20,
        'Side': '1',
        'CashMargin': 3,
        'MarginTradeType': 2,
        'DelivType': 2,
        'AccountType': 2,
        'Qty': 100,
        'ClosePositionOrder': 1,
        'Price': 2762.5,
        'ExpireDay': 20200924 }
json_data = json.dumps(obj).encode('utf-8')

url = 'http://localhost:18080/kabusapi/sendorder'
req = urllib.request.Request(url, json_data, method='POST')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)
#（３）返済（返済建玉指定） コマンド：python kabusapi_sendorder_margin_pay_ClosePositions.py

obj = { 'Password': '123456',
        'Symbol': '9433',
        'Exchange': 1,
        'SecurityType': 1,
        'FrontOrderType': 20,
        'Side': '1',
        'CashMargin': 3,
        'MarginTradeType': 1,
        'DelivType': 2,
        'AccountType': 4,
        'Qty': 200,
        'ClosePositions': [{'HoldID':'E20200924*****','Qty':100},{'HoldID':'E20200924*****','Qty':100}],
        'Price': 2762.5,
        'ExpireDay': 20200924 }
json_data = json.dumps(obj).encode('utf-8')

url = 'http://localhost:18080/kabusapi/sendorder'
req = urllib.request.Request(url, json_data, method='POST')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
４．注文発注（先物）
'''
#（１）新規 コマンド：python kabusapi_sendorder_future_new.py
obj = { 'Password': '123456',
        'Symbol': '165120018',
        'Exchange': 23,
        'TradeType': 1,
        'TimeInForce': 1,
        'Side': '1',
        'Qty': 3,
        'Price': 22000,
        'ExpireDay': 20200925,
        'FrontOrderType': 20 }
json_data = json.dumps(obj).encode('utf-8')

url = 'http://localhost:18080/kabusapi/sendorder/future'
req = urllib.request.Request(url, json_data, method='POST')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)
#（２）返済（決済順序） コマンド：python kabusapi_sendorder_future_pay_ClosePositionOrder.py
#（３）返済（返済建玉指定） コマンド：python kabusapi_sendorder_future_pay_ClosePositions.py
'''
５．注文発注（OP））
'''
#（１）新規 コマンド：python kabusapi_sendorder_option_new.py
obj = { 'Password': '123456',
        'Symbol': '145123218',
        'Exchange': 23,
        'TradeType': 1,
        'TimeInForce': 2,
        'Side': '1',
        'Qty': 5,
        'Price': 0,
        'ExpireDay': 20200924,
        'FrontOrderType': 120 }
json_data = json.dumps(obj).encode('utf-8')

url = 'http://localhost:18080/kabusapi/sendorder/option'
req = urllib.request.Request(url, json_data, method='POST')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)
#（２）返済（決済順序） コマンド：python kabusapi_sendorder_option_pay_ClosePositionOrder.py
#（ ３）返済（返済建玉指定） コマンド：python kabusapi_sendorder_option_pay_ClosePositions.py

'''
６．注文取消 コマンド：
'''
#注文取消 コマンド：python kabusapi_cancelorder.py
obj = { 'OrderID': '20200709A02N04712032', 'Password': '123456' }
json_data = json.dumps(obj).encode('utf8')

url = 'http://localhost:18080/kabusapi/cancelorder'
req = urllib.request.Request(url, json_data, method='PUT')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
７．取引余力（現物） コマンド
'''
#取引余力（現物） コマンド：python kabusapi_cash.py


url = 'http://localhost:18080/kabusapi/wallet/cash'
req = urllib.request.Request(url, method='GET')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
８．取引余力（信用） コマンド
'''
#取引余力（信用） コマンド：python kabusapi_margin.py
url = 'http://localhost:18080/kabusapi/wallet/margin'
req = urllib.request.Request(url, method='GET')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
９．取引余力（先物） コマンド
'''
#取引余力（先物） コマンド：python kabusapi_wallet_future.py

url = 'http://localhost:18080/kabusapi/wallet/future'
req = urllib.request.Request(url, method='GET')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
10．取引余力（OP） コマンド
'''
#python kabusapi_wallet_option.py
url = 'http://localhost:18080/kabusapi/wallet/option'
req = urllib.request.Request(url, method='GET')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)
'''
11．時価情報・板情報 コマンド
'''
#python kabusapi_board.py
url = 'http://localhost:18080/kabusapi/board/5401@1'
req = urllib.request.Request(url, method='GET')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
12．銘柄情報
'''
#python kabusapi_symbol.py

url = 'http://localhost:18080/kabusapi/symbol/5401@1'
req = urllib.request.Request(url, method='GET')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
13．注文約定照会 コマンド
'''
#：python kabusapi_orders.py
url = 'http://localhost:18080/kabusapi/orders'
params = { 'product': 0 }               # product - 0:すべて、1:現物、2:信用、3:先物、4:OP
#params['id'] = '20201207A02N04830518' # id='xxxxxxxxxxxxxxxxxxxx'
#params['updtime'] = 20201101123456    # updtime=yyyyMMddHHmmss
#params['details'] =  'false'          # details='true'/'false'
#params['symbol'] = '9433'             # symbol='xxxx'
#params['state'] = 5                   # state - 1:待機（発注待機）、2:処理中（発注送信中）、3:処理済（発注済・訂正済）、4:訂正取消送信中、5:終了（発注エラー・取消済・全約定・失効・期限切れ）
#params['side'] = '2'                  # side - '1':売、'2':買
#params['cashmargin'] = 3              # cashmargin - 2:新規、3:返済

req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', '37b96984a496419ebc2abcffa29728d4')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
14．残高照会 コマンド
'''
#python kabusapi_positions.py
url = 'http://localhost:18080/kabusapi/positions'
params = { 'product': 0 }   # product - 0:すべて、1:現物、2:信用、3:先物、4:OP
#params['symbol'] = '9433'  # symbol='xxxx'
req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', '43e7cc3611fd476db35e93c36a3f77ef')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
15．先物銘柄コード取得 コマンド
'''
#python kabusapi_symbolname_future.py
url = 'http://localhost:18080/kabusapi/symbolname/future'
params = { 'FutureCode': 'NK225', 'DerivMonth': 202012 }

req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e
'''
16．オプション銘柄コード取得 コマンド
'''
#python kabusapi_symbolname_option.py
url = 'http://localhost:18080/kabusapi/symbolname/option'
params = { 'DerivMonth': 202012, 'PutOrCall': 'C', 'StrikePrice': 24000 }

req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
17．PUSH配信開始 コマンド
'''
#python kabusapi_websocket.py
import sys
import websocket
import _thread

def on_message(ws, message):
    print('--- RECV MSG. --- ')
    print(message)

def on_error(ws, error):
    print('--- ERROR --- ')
    print(error)

def on_close(ws):
    print('--- DISCONNECTED --- ')

def on_open(ws):
    print('--- CONNECTED --- ')
    def run(*args):
        while(True):
            line = sys.stdin.readline()
            if line != '':
                print('closing...')
                ws.close()
    _thread.start_new_thread(run, ())

url = 'ws://localhost:18080/kabusapi/websocket'
# websocket.enableTrace(True)
ws = websocket.WebSocketApp(url,
                          on_message = on_message,
                          on_error = on_error,
                          on_close = on_close)
ws.on_open = on_open
ws.run_forever()
'''
18．銘柄登録 コマンド
'''
#python kabusapi_register.py
obj = { 'Symbols':
        [ 
            {'Symbol': '9433', 'Exchange': 1},
            {'Symbol': '165120018', 'Exchange': 2},
            {'Symbol': '145123218', 'Exchange': 2}
        ] }
json_data = json.dumps(obj).encode('utf8')

url = 'http://localhost:18080/kabusapi/register'
req = urllib.request.Request(url, json_data, method='PUT')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
19．銘柄登録解除 コマンド
'''
#python kabusapi_unregister.py
obj = { 'Symbols':
        [ 
            {'Symbol': '9433', 'Exchange': 1},
            {'Symbol': '165120018', 'Exchange': 2},
            {'Symbol': '145123218', 'Exchange': 2}
        ] }
json_data = json.dumps(obj).encode('utf8')

url = 'http://localhost:18080/kabusapi/unregister'
req = urllib.request.Request(url, json_data, method='PUT')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)

'''
20．銘柄登録全解除 コマンド
'''
#python kabusapi_unregisterall.py
url = 'http://localhost:18080/kabusapi/unregister/all'
req = urllib.request.Request(url, method='PUT')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', 'ed94b0d34f9441c3931621e55230e402')
# req.add_header('Content-Length', 0)

try:
    with urllib.request.urlopen(req) as res:
        print(res.status, res.reason)
        for header in res.getheaders():
            print(header)
        print()
        content = json.loads(res.read())
        pprint.pprint(content)
except urllib.error.HTTPError as e:
    print(e)
    content = json.loads(e.read())
    pprint.pprint(content)
except Exception as e:
    print(e)
