import urllib.request
import json
import pprint

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