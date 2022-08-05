import os
import parsel
import requests
from tqdm import tqdm
from random import randint
from time import time, sleep
from requests.exceptions import RequestException


class DownloadBiQuGe:
    """爬取笔趣阁:http://www.b5200.net或者org"""

    def __init__(self):
        self.novel_name = ''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/95.0.4638.69 Safari/537.36'
        }
        if not os.path.exists('.\\笔趣阁'):
            os.mkdir('.\\笔趣阁')

    def __requestes(self, url, params=None):
        """获取网页数据"""
        with requests.get(url=url, headers=self.headers, params=params) as response:
            response.encoding = 'gbk'
        return response

    def get_url_data(self, url, params=None):
        """网络爬取处理异常"""
        try:
            return self.__requestes(url, params=params)
        except RequestException as e:
            print(f'\n爬取{url}时出现异常：{e}')
            del e
            seconds = randint(10, 30)
            print(f'休息 {seconds} 秒后重试...')
            sleep(seconds)
            try:
                print('开始重试...')
                return self.__requestes(url, params=params)
            except RequestException as e:
                print(f'\n爬取{url}时发生错误：{e}')
                del e
                print('重试后仍然无法解决，程序退出！')

    def get_table_of_contents_url(self, url):
        """
        获取小说的全部章节目录的url
        url:小说的目录网址
        返回小说所有章节的url列表
        """
        response = self.get_url_data(url)
        selector = parsel.Selector(response.text)
        urls_list = selector.css('#list dl dd a::attr(href)').getall()[9:]  # 0-8为最新章节
        # print(url_list)
        return urls_list

    def get_one_chapter(self, url):
        """爬取1个章节，调用保存函数"""
        response = self.get_url_data(url)
        if response:
            selector = parsel.Selector(response.text)
            title = selector.css('.bookname h1::text').get()  # 获取 章节标题
            table = title.maketrans(r'\*"/:?|<>', '         ')
            title = title.translate(table).replace(' ', '')
            contents = selector.css('#content p::text').getall()  # 获取 文章文本类容
            text = ''
            # print(contents)
            for i in contents:
                text += i.strip() + '\n'
            # print(text)
            if self.save_to_txt(title, text):
                print(f'{title}')

    def do_search_book(self, book_name):
        """搜索小说名或者作者名,并调用搜索结果显示函数,返回parsel.Selector"""
        url = f'http://www.b5200.org/modules/article/search.php'
        params = {
            'searchkey': book_name
        }
        response = self.get_url_data(url, params=params)
        selector = parsel.Selector(response.text)
        self.show_search_resul(selector)  # 调用搜索结果显示函数
        return selector

    @staticmethod
    def show_search_resul(selector):
        """显示搜索到的小说或作者名称"""
        resul_title = selector.css('.odd a::text').getall()
        if not resul_title:  # 没有搜索结果
            print('出错啦。没找到相关的小说或作者')
        else:
            resul_url = selector.css('.odd a::attr(href)').getall()
            resul_author = selector.css('.odd::text').getall()[::2]  # 只要作者，最后更新时间等不要
            # print(resul_title, resul_url, resul_author)
            resul_num = len(resul_title)  # 搜索结果 个数
            print(f'搜索到相关内容{resul_num}个：')
            for i in range(resul_num):
                print(f'{(i + 1)}. <<{resul_title[i]}>>\t作者：{resul_author[i]}\t 目录地址：{resul_url[i]}')

    @staticmethod
    def get_choose():
        """获取用户的选择，并返回选择的整数"""
        while True:
            choose = input('你要下载第几个？请选择：')
            if choose.isalpha() or choose.isspace():
                print('你的输入有误！请重新选择：')
            else:
                return int(choose) - 1  # 显示的时候加了1，这里需要减回来

    def get_search_key(self):
        """获取用户的输入书名或者作者名,返回搜索结果"""
        search_key = input('请输入您要下载的小说或作者的名称：')
        result = self.do_search_book(search_key)
        return result

    def save_to_txt(self, title, text):
        """保存文本"""
        try:
            with open(f'.\\笔趣阁\\{self.novel_name}\\{title}.txt', mode='w', encoding='utf-8') as f:
                f.write(text)
        except IOError as e:
            print(f'保存{title}.txt 时发生错误：：{e}')
            return False
        except Exception as ee:
            print(ee)
        else:
            return True

    def task(self):
        """开启书本下载任务"""
        star_time = time()
        result = self.get_search_key()  # 会逐级返回搜索结果
        resul_url = result.css('.odd a::attr(href)').getall()  # 在搜索结果中取目录网址
        resul_title = result.css('.odd a::text').getall()  # 在搜索结果中取小说名
        choose = self.get_choose()  # 用户选择下载第几个

        self.novel_name = resul_title[choose]
        if not os.path.exists(f'.\\笔趣阁\\{self.novel_name}'):
            os.mkdir(f'.\\笔趣阁\\{self.novel_name}')

        urls_list = self.get_table_of_contents_url(resul_url[choose])  # 章节目录列表
        print(f'一共{len(urls_list)}章节，请耐心等待...')

        for url in tqdm(urls_list, colour='green'):
            self.get_one_chapter(url)
            sleep(0.85)
        print(f'任务完成.耗时{(time() - star_time):.2f}秒')


d = DownloadBiQuGe()  # 实列化
d.task()  # 开启任务