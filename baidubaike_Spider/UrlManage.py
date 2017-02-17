#coding:utf-8

class UrlManage(object):

	#初始化兩個set，一個存放已經遍歷的url，一個存放還沒有遍歷的url
	def __init__(self):
		self.new_urls_set=set()
		self.old_urls_set=set()

	#將新的url加入 new_urls_set
	def add_newurl(self,url):
		if url is None:
			return 
		if url not in self.new_urls_set and url not in self.old_urls_set:
			self.new_urls_set.add(url)

	#將一個新的url結合（set類型）加入到new_urls_set
	def add_newurl_set(self,urlset):
		if urlset is None:
			return 
		for url in urlset:
			self.add_newurl_set(url)

	#判斷new_urls_set是否是空
	# 和源碼不一樣
	def is_newurlsset_empty(self):
		if self.new_urls_set is None:
			return True;
		return False;


	#從new_urls_set獲得一個新的url
	def get_new_url(self):
		url=self.new_urls_set.pop()
		self.old_urls_set.add(url)
		return url
