from urllib3 import PoolManager


# for all browser
def url_login(driver, username, pwd):
    print("start sign in")
    url = 'https://mfcentral.manulife.com/login?startURL=%2Fcms__main'
    str_before_flag = '<form id="options"  method="post" action="'
    str_after_flag = '">\r\n            <script type="text/javascript">\r\n'
    http = PoolManager()
    res = http.request(method='GET', url=url)
    body = res.data.decode("utf-8")
    url2 = body.split(str_before_flag)[1].split(str_after_flag)[0]
    url3 = url2[:37] + 'wia' + url2[37:]
    url2_auth = url3[:8] + username + ':' + pwd + '@' + url3[8:]
    driver.get(url2_auth)
    print("finish sign in")
