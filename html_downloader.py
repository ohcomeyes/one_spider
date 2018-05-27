from urllib import request
from urllib.parse import quote
import string
class HtmlDownLoader:


    # 下载页面内容
    def downloade(self,new_url):
        if(new_url is None):
            return None
        # 解决请求路径中含义中文或特殊字符
        url_ = quote(new_url, safe=string.printable);
        # 这是代理IP
        proxy = {'http': '115.198.35.175:6666'}
        # 创建ProxyHandler
        proxy_support = request.ProxyHandler(proxy)
        # 创建Opener
        opener = request.build_opener(proxy_support)
        # 添加User Angent
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:60.0) Gecko/201')]
        # 安装OPener
        request.install_opener(opener)
        # 使用自己安装好的Opener
        response = request.urlopen(url_)
        if(response.getcode()!=200):
            return None #请求失败
        html = response.read()
        return html.decode("utf8")