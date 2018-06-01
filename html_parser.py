from bs4 import BeautifulSoup
import re
from urllib import parse


class HtmlParser:
    # 构造函数 初始化
    def __init__(self):
        # 实例化需引用的对象
        self.new_datas = []
        self.old_origin_url = []
        self.new_origin_url = {}
    # page_url 基本url 需拼接部分
    def _get_new_urls(self, soup):
        new_urls = set()
        # 匹配 /item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6
        links = soup.find('div', class_='page_navi')
        for link in links.find_all('a'):
            new_url = link["href"]
            # 例如page_url=http://baike.baidu.com/item/Python new_url=/item/史记·2016?fr=navbar
            # 则使用parse.urljoin(page_url,new_url)后 new_full_url = http://baike.baidu.com/item/史记·2016?fr=navbar
            #new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_url)
        return new_urls

    # 二级明细页面获取
    def _get_origin_urls(self, page_url, soup):
        data = soup.find(class_='article-content')
        print(data.text.replace("\n", "").strip())
        self.new_origin_url[page_url] = data.text.replace("\n", "").strip()


    # 所有数据添加到数据集中
    def _get_new_data(self, soup):
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        datas = soup.find_all(class_='image-container')
        for data in datas:
            new_data = {}
            new_data['url'] = 'https://8xda.com/d/'+data.a.get('href').split('/')[4]
            new_data['title'] = data.find(class_='postTitle').text
            new_data['date'] = data.div.text
            self.old_origin_url.append(new_data['url'])
            self.new_datas.append(new_data)

    def parse(self, page_url, html_context, page=1):
        if (page_url is None or html_context is None):
            return
            # python3缺省的编码是unicode, 再在from_encoding设置为utf8, 会被忽视掉，去掉【from_encoding = "utf-8"】这一个好了
        soup = BeautifulSoup(html_context, "html.parser")
        if page == 1:
            new_urls = self._get_new_urls(soup)
            self._get_new_data(soup)
            return new_urls
        else:
            self._get_origin_urls(page_url,soup)