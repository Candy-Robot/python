import requests

if __name__ == '__main__':
    target = 'https://www.xsbiquge.com/15_15338/8549128.html'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    print(req.text)
