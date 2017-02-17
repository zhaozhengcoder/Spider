#coding:utf-8
import HtmlParse,UrlManage,html_outputer,html_download3

class SpiderMain(object):
	def __init__(self):
		#第一個是模塊的名字，第二個是模塊內部對象的名字
		#html_download.HtmlDownload()
		self.html_download=html_download3.HtmlDownload()
		self.html_parser=HtmlParse.HtmlParse()
		self.urlmanage=UrlManage.UrlManage()
		self.html_output=html_outputer.HtmlOutputer()

	def spider(self,root_url):
		count=1
		self.urlmanage.add_newurl(root_url)
		url=self.urlmanage.get_new_url()

		print ('catch %d : %s' % (count,url))
		#print ('craw %d : %s' % (count, new_url))
		html_content=self.html_download.download(url)

		new_urls,new_data=self.html_parser.parser(url,html_content)
		self.html_output.collect_data(new_data)
		self.html_output.output_html()

if __name__=='__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
    print ("can nim a    !!!")
    obj_spider = SpiderMain()
    obj_spider.spider(root_url)