# 创建类
import url_manager, html_downloader, html_output, html_parser
import numpy as np
import time

class spiderMain:
    # 构造函数 初始化
    def __init__(self):
        # 实例化需引用的对象
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.output = html_output.HtmlOutPut()
        self.parser = html_parser.HtmlParser()
        self.errorList = []

    def craw(self, root_url):
        # 添加一个到url中
        self.urls.add_new_url(root_url)
        # 爬两页
        page_count = 10
        count = 1
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            try:
                # 休息会
                time.sleep(2)
                print('craw %d : %s' % (count, new_url))
                # 下载
                html_context = self.downloader.downloade(new_url, count)
                new_urls = self.parser.parse(new_url, html_context, 1 if count <= page_count else 2)
                if count < page_count:
                    self.urls.add_new_urls(new_urls)
                elif count == page_count:
                    # 爬完后清空页码url
                    self.urls.new_urls.clear()
                    self.urls.add_new_urls(self.parser.old_origin_url)
                count += 1
                print(self.urls.new_urls)
            except Exception as e:
                print('Error:%s url:%s' % (e, new_url))
                time.sleep(10)
                self.craw(new_url)
        self.output.urls, self.output.datas = self.parser.new_origin_url,self.parser.new_datas
        self.output.output_html()

    # 创建main方法

if __name__ == "__main__":
    # https://8xdb.com/html/83445
    root_url = "https://8xda.com/html/category/video"
    spiderMain().craw(root_url)
