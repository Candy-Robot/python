import urllib.request
import os

#打开链接
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()

    return html

#得到页码
def get_page(url):
    #强制解码为utf-8的形式
    html = url_open(url).decode('utf-8')

    #查找需要找的位置 +23是偏移的位置，23是在23位
    a = html.find('') + 23
    #从a的位置找到下一个方括号
    b = html.find(']',a)

    return html[a:b]

def find_imgs(url):
    #打开链接
    html = url_open(url).decode('utf-8')
    #申明列表，把找到的图片都放到这个列表之中
    img_addrs = []
    #查找图片
    a = html.find('img src=')
    
    while a != -1:
        #从a开始找.jpg 如果没有找到最多找到位置在a+255的地方
        b = html.find('.jpg', a, a+255)
        #如果没有找到b会返回-1
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9 #如果没有找到b，就要让b的地址变化一下，不然会无限循环
        #a从b结束的地方开始找
        a = html.find('img src=',b)

    return img_addrs

#保存图片  
def save_imgs(folder,img_addrs):
    for each in img_addrs:
        #取得文件的名字
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            #把文件写进去打开链接
            img = url_open(each)
            f.write(img)

def download_mm(folder='ooxx',pages=3):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx"
    #找到关于页码的字符串，并把页码的字符串转换为整形给page_num
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i

        #用得到的page_num和网页上找到的字符串拼成page_url
        page_url = url + 'MjAyMDA0MDctMTc'+str(i) + '#comments'

        #打开链接找到图片，运用find_imgs的函数
        img_addrs = find_imgs(page_url)

        #保存图片到folder文件夹中
        save_imgs(folder,img_addrs)


if __name__ == '__main__':
    download_mm()
