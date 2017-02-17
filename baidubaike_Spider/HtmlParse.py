#coding:utf-8
import requests
from bs4 import BeautifulSoup
import re

class HtmlParse(object):
	#從soup裏面提去特定的url
	#page_url 是http://www.baike.baidu.com/
	#因爲後面獲得的是相對地址
	def get_new_urlset(self,page_url,soup):
		new_urlset=set()
		links=soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
		for link in links:
			new_url=link['href']
			new_full_url=page_url+new_url
			new_urlset.add(new_full_url)
		return new_urlset

	#從soup裏面特定的內容
	def get_new_data(self,page_url,soup):
		#創建一個map
		res_data={}
		res_data['url']=page_url
		# <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
		title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
		res_data['title'] = title_node.get_text()
		
		#print ('title  >>',res_data['title']) 
		# <div class="lemma-summary" label-module="lemmaSummary">
		summary_node = soup.find('div', class_='lemma-summary')
		res_data['summary'] = summary_node.get_text()
		#print ('res_data >>',res_data['summary'])
		#print(res_data)
		return res_data


	#從html_content 裏 ，利用get_new_url 函數和 get_new_data提取url和data
	def parser(self,page_url,html_content):
		soup=BeautifulSoup(html_content,'html.parser')
		new_urlset=self.get_new_urlset(page_url,soup)
		new_data =self.get_new_data(page_url,soup)
		return new_urlset,new_data

if __name__=='__main__':
	url='http://baike.baidu.com/view/21087.htm'
	page_url='http://baike.baidu.com'
	page=requests.get(url)

	#print page.text

	hp=HtmlParse()
	url_set,datas=hp.parser(page_url,page.text)

	#for url in url_set:
	#	print (url)

	#for data in datas:
	#	print (data)