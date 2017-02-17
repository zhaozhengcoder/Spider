#coding:utf-8
import requests
import urllib.request

# 注意這個亂碼的分析 用這個文件解釋的時候，得到的就是亂碼
# 但是用Html_download2 執行的時候，就不是亂碼
# 真的是 
class HtmlDownload(object):
    def download(self, url):
        if url is None:
            return None
        response = requests.get(url)
        if response.status_code!= 200:
            return None
        #得到html 的全部內容
        return response.text