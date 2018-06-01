class HtmlOutPut:
    def __init__(self):
        self.urls = {}  # 存放搜集的url
        self.datas = []  # 存放搜集的数据

    def collect_data(self, new_data):
        if (new_data is None):
            return
        self.datas.append(new_data)

    def output_html(self):
        fout = open('output.html', 'a', encoding='utf8')  # 写入文件 防止中文乱码
        fout.write('<html><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
        fout.write('<body>\n')
        fout.write('<table>\n')
        for data in self.datas:
            fout.write('<tr>\n')
            fout.write('<td>%s</td>\n' % self.urls[data['url']])
            fout.write('<td>%s</td>\n' % data['title'])
            fout.write('<td>%s</td>\n' % data['date'])
            fout.write('</tr>\n')
        fout.write('</table>\n')
        fout.write('</body>\n')
        fout.write('</html>\n')
        fout.close()