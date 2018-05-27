# encoding: utf-8
import urllib.parse
import urllib.request
import json
from urllib import request

from lxml import html


def get_page(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0"'
    values = {'name' : 'Michael Foord',
              'location' : 'Northampton',
              'language' : 'Python' }
    headers = { 'User-Agent' : user_agent }
    data = urllib.parse.urlencode(values)
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    # print(response)
    return parse(response.read())


def paging():
    ip_dict = {}
    for page in range(1, 11):
        url = "https://www.xicidaili.com/nn/{}".format(page)
        ip_dict[page] = get_page(url)
        print(ip_dict)
    data = json.dumps(ip_dict)
    with open('ip.json', 'a+') as f:
        f.write(data)


def parse(html):
    list_ip = []
    contents = html.xpath("//table[@id='ip_list']/tr[position()>1]")
    for content in contents:
        ip = content.xpath("./td[2]/text()")[0]
        port = content.xpath("./td[3]/text()")[0]
        mold = content.xpath("./td[6]/text()")[0]
        # print(ip, port, mold)
        list_ip.append(mold.lower() + ':' + ip + ":" + port)
    return list_ip


if __name__ == '__main__':
    # paging()
    # 访问网址
    url = 'http://ip.chinaz.com/'
    # 这是代理IP
    proxy = {'http': '115.198.35.175:6666'}
    # 创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    # 创建Opener
    opener = request.build_opener(proxy_support)
    # 添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:60.0) Gecko/201')]
    # 安装OPener
    request.install_opener(opener)
    # 使用自己安装好的Opener
    response = request.urlopen(url)
    # 读取相应信息并解码
    html = response.read().decode("utf-8")
    # 打印信息
    print(html)
