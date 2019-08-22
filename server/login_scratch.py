from urllib3 import PoolManager
from urllib3.util import make_headers

url = 'https://mfcentral.manulife.com/login?startURL=%2Fcms__main'

http = PoolManager()

res = http.request(method='GET', url=url)
body = res.data.decode("utf-8")
strBeforeFlag = '<form id="options"  method="post" action="'
strAfterFlag = '">\r\n            <script type="text/javascript">\r\n'
url2 = body.split(strBeforeFlag)[1].split(strAfterFlag)[0]

url3 = url2[:37] + 'wia' + url2[37:]

url2Auth = url3[:8] + 'tongzhi:$$Bill990226@' + url3[8:]
print(url2Auth)
res2 = http.request(method='GET', url=url2Auth)
print(res2.data.decode("utf-8"))