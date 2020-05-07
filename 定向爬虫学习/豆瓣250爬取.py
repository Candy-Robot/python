import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "movie.douban.com",
    "Referer": "https://movie.douban.com/explore",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/55.0.2883.87 Safari/537.36"
}


def request_douban(web_url):
    # noinspection PyBroadException
    try:
        r = requests.get(url=web_url, header=headers)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return "发生异常"


def save_to_txt(soup):
    f = open("douban.txt", "a")

    list_douban = soup.find(class_='grid_view').find_all('li')
    for item in list_douban:
        item_name = item.find(class_='title').string
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_intr = item.find(class_='inq').string

        f.write(item_index + '、')
        f.write(item_name + "\n")
        f.write(item_score + "\n")
        f.write(item_intr)
        f.write("\n\n")


def main(page):
    url = 'https://movie.douban.com/top250?start=' + str(page*25)+'&filter='
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    save_to_txt(soup)


if __name__ == '__main__':
    for i in range(0, 10):
        main(i)

