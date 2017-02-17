# coding:utf-8
import urllib.request

class HtmlDownload(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        #得到html 的全部內容
        return response.read()