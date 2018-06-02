import requests
import os
import re
import random
import time
from ip import ProxyId

def download_mm(pages=25):
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
        img_urls = get_img_url(page_url)
        for img_url in img_urls:
            img_addrs = find_images(img_url)
            save_imgs(img_addrs)

def get_img_url(url):
    # 爬取当前html页面内容
    html = url_open(url).text
    # 找出包含图片源地址的这一段字符串
    res_url = r'(?<=href=\").+?com\/html\/\d+(?=\")|(?<=href=\').+?com\/html\/\d+(?=\')'
    url_list = re.findall(res_url, html)  # 有重复数据
    return set(url_list)

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
    img_src0 = re.findall(r'(?<=img\ssrc=\").+?com\/p\/\d.+?(?=\")', html)
    # 从包含图片源地址的这一段字符串中提取图片的源地址
    # img_src1=[img_src[10:] for img_src in img_src0]
    return img_src0

def save_imgs(img_addrs):
    """
    保存图片
    """
    for img_addr in img_addrs:
        # 将图片地址的倒数第二个字符串作为图片名
        filename=img_addr.split('/')[-2]+'_'+img_addr.split('/')[-1]
        # 休息会
        time.sleep(1)
        # 以二进制的方式(content而非text)保存图片源地址内容
        img=url_open('{}'.format(img_addr)).content
        with open(filename,'wb') as f:
             f.write(img)
             print('image:%s save success' % (filename))
             f.close()

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
    download_mm()
    '''
    html = '<div class="col-xs-6 col-sm-6 col-md-4 contentItem"><div class="image-container"><a href="https://8xdb.com/html/84768" target="_blank"><img width="342" height="208" src="https://lucky.sxspic.com/p/2018/06/01212437/2018-06-01_13-24-37_144197.jpg" class="attachment-342x208 size-342x208 " alt="" /></a><a href="https://8xdb.com/html/84768" class="postTitle" target="_blank">长腿丝袜美眉丰满身材写真</a><div class="updateStamp">2018-06-02<span class="timeStamp">8P</span></div></div></div>\
            <div class="col-xs-6 col-sm-6 col-md-4 contentItem"><div class="image-container"><a href="https://8xdb.com/html/84779" target="_blank"><img width="342" height="208" src="https://lucky.sxspic.com/p/2018/06/01212946/2018-06-01_13-29-46_016649.jpg" class="attachment-342x208 size-342x208 " alt="" /></a><a href="https://8xdb.com/html/84779" class="postTitle" target="_blank">护士装美女与情趣装美女暧昧图-03</a><div class="updateStamp">2018-06-02<span class="timeStamp">8P</span></div></div></div>\
            <li><a href="https://8xdb.com/html/category/video/video5" >3</a></li>\
            <link rel="shortcut icon" href="/favicon.ico">'
    url = re.findall(r'<a\shref=.*?</a>', html)
    res_url = r'(?<=href=\").+?com\/html\/\d+(?=\")|(?<=href=\').+?com\/html\/\d+(?=\')'
    url_list = re.findall(res_url, html)
    print(set(url_list))
    html = '<p><img src="https://lucky.sxspic.com/p/20170820220959/3-1.jpg" alt="" width="1126" height="1501" class="aligncenter size-full " /></p> \
            <p><img src="https://lucky.sxspic.com/p/20170820221002/4-1.jpg" alt="" width="1126" height="844" class="aligncenter size-full " /></p> \
            <img src="https://lucky.sxspic.com/p/img/logo_2018.png"/><img src="https://lucky.sxspic.com/p/img/logo_2018.png" style="height:50px; width:auto;"/>'
    img_src0 = re.findall(r'(?<=img\ssrc=\").+?com\/p\/\d.+?(?=\")', html)
    print(img_src0)
    '''