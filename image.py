import requests
import os
import re
import random
from ip import ProxyId

def download_mm(folder='mmImages', pages=10):
    """
    下载十个页面的图片,并将其保存进folder目录
    """
    # 创建保存图片的文件夹
    if not os.path.exists('folder'):
        os.mkdir('folder')
    os.chdir('folder')
    # 下载图片页面初始地址
    # url = 'http://jandan.net/ooxx/'
    url = 'https://8xdb.com/html/category/photo'
    # 图片页面地址全名为http://jandan.net/ooxx/page-2364#comments,可看出图片地址为'url'+'页面数'+ '#comments',先定义一个函数get_page(url)来获取page_num
    # page_num = int(get_page(url))
    page_num = 25
    for i in range(pages):
        page_num -= i
        page_url = url + '/page/' + str(page_num)
        img_addrs = find_images(page_url)
        save_imgs(folder, img_addrs)

def get_page(url):
    """
    返回单前网页page数,也即url = 'http://jandan.net/ooxx/'的page数
    """
    # 爬取html页面内容
    html= url_open(url).text
    # 找出含有本页网址的那一段字符串
    page=re.search(r'>\[[0-9]{4}\]<',html)
    # 从这一段字符串提取出页面数
    page_number=re.search(r'[0-9]{4}',page).group()
    return page_number

def find_images(url):
    """
    找到图片的源地址
    """
    # 爬取当前html页面内容
    html=url_open(url).text
    # 找出包含图片源地址的这一段字符串
    img_src0=re.findall(r'<img\ssrc=.{,80}.[jpg|png|gif]',html)
    # 从包含图片源地址的这一段字符串中提取图片的源地址
    img_src1=[img_src[10:] for img_src in img_src0]
    return img_src1

def save_imgs(folder, img_addrs):
    """
    保存图片
    """
    for img_addr in img_addrs:
        # 将图片地址的倒数第二个字符串作为图片名
        filename=img_addr.split('/')[-1]
        # 以二进制的方式(content而非text)保存图片源地址内容
        img=url_open('http:{}'.format(img_addr)).content
        with open(filename,'wb') as f:
             f.write(img)

def url_open(url):
    """
    爬取网页
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Referer': 'https://8xdb.com/html/category/photo'
    }
    proxy = {'http': random.choice(ProxyId().ips)}
    req = requests.get(url, headers=headers, proxies=proxy, timeout=20)
    return req

if __name__ == "__main__":
    download_mm(pages=1)