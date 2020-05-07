
import urllib.request
import urllib.parse
import json
import time

while True:
    content = input("请输入需要翻译的内容(输入'q'退出程序)： ")
    if content == 'q':
        break
    """
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    """

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['i']=content
    data['from']='AUTO'
    data['to']= 'AUTO'
    data['smartresult']= 'dict'
    data['client']= 'fanyideskweb'
    data['salt']='15861706832761'
    data['sign']='df57b0f7aedd046d84b5f1e8a9cb32ca'
    data['ts']= '1586170683276'
    data['bv']='e3024dc52ff5c694b77471a08006ba92'
    data['doctype']= 'json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']= 'FY_BY_REALTlME'
    data =  urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36')

    response = urllib.request.urlopen(req) 
    html = response.read().decode('utf-8')

    target = json.loads(html)
    answer = target['translateResult'][0][0]['tgt']
    print(answer)

    time.sleep(5)
