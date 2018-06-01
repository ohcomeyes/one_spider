from urllib import request
from urllib import error
from urllib.parse import quote
import requests
import random
from ip import ProxyId
import string


class HtmlDownLoader:
    def __init__(self):
        self.hds = [
            ('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'),
            ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'),
            ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:60.0) Gecko/201')
        ]
        self.user_agent_list = [
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:60.0) Gecko/201',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
        ]

    # 下载页面内容
    def downloade(self, new_url, count):
        if(new_url is None):
            return None
        headers = {'User-Agent': random.choice(self.user_agent_list), "Referer": "https://8xda.com/html/category/video"}
        # 解决请求路径中含义中文或特殊字符
        url_ = quote(new_url, safe=string.printable)
        # 这是代理IP
        proxy = {'http': random.choice(ProxyId().ips)}
        # 创建ProxyHandler
        # proxy_support = request.ProxyHandler(proxy)
        # 创建Opener
        # opener = request.build_opener(proxy_support)
        # 添加User Angent
        # opener.addheaders = [self.hds[count % len(self.hds)]]
        # 安装OPener
        # request.install_opener(opener)
        # 使用自己安装好的Opener
        response = requests.get(url_, headers=headers, proxies=proxy, timeout=20)
        # response = request.urlopen(url_)
        if (response.status_code != 200):
            return None  # 请求失败
        #html = response.read()
        #return html.decode("utf8")
        response.encoding = "utf-8"
        return response.text