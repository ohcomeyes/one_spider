# encoding: utf-8
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import random
import string
import json
import os
import xmlrpc.client as xc
from urllib import request

from pyaria2 import PyAria2


class ProxyId:
    ips = []
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
            'Referer': 'http://www.xicidaili.com/'
        }
        if not ProxyId.ips:
            self.visit()

    def visit(self):
        print("去抓取")
        url = 'http://www.xicidaili.com/nn'  # 西刺代理扒拉下来的
        rq = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(rq)
        self.parse(response.read())

    def parse(self, html):
        list_ip = []
        soup = BeautifulSoup(html, "html.parser")
        datas = soup.find_all('tr', class_='odd')
        for data in datas:
            tds = data.findAll('td')
            ProxyId.ips.append(tds[1].text+':'+tds[2].text)


if __name__ == '__main__':
    pya = PyAria2()
    with open('output.html', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        dates = soup.find_all('td')
        for data in dates:
            if 'mp4' in data.text:
                urls = []
                urls.append(data.text)
                pya.addUri(urls)
    # print(os.environ['PATH'])
    # print(urls)
    # url = ['http://d.b612kj.com/assets/7b5954466442c9a1d16e8a37003a28aa.mp4']
    # pya.addUri(url)
