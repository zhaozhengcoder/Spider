#coding:utf-8
import requests
import urllib.request
#import sys    
#python3 沒有這個庫 


# 注意這個亂碼的分析 用這個文件解釋的時候，得到的就是亂碼
# 但是用Html_download2 執行的時候，就不是亂碼
# 真的是 

#reload(sys)
#sys.setdefaultencoding('utf-8')
"""
class HtmlDownload2(object):
	def download(self,url):
		print ('>>>',url)

		if url is None:
			return None
		page=requests.get(url)

		#python3 的特有的語法 print()
		print ("encoding :")
		print (page.encoding)
		if page.status_code!=200:
			return None

		#print ("type : ")
		#print (type(page.text))
		#print ("####>>>>> test")
		#print (page.headers['content-type'])
		#print ('內容的編碼格式：',page.encoding)
		#print ('頭部的編碼格式:',page.apparent_encoding)
		#print ('html 標籤中頭部設置的內容編碼格式 :',requests.utils.get_encodings_from_content(page.text)) 
		#print ("####>>>>> test")
		#if page.encoding == 'ISO-8859-1':
		#	encodings = requests.utils.get_encodings_from_content(page.text)
		#	if encodings:
		#		encoding = encodings[0]
		#	else:
		#		encoding = page.apparent_encoding
		# = page.content.decode(encoding, 'replace').encode('utf-8', 'replace')
		#
		#print (encode_content)
		return page.text

"""
class HtmlDownload(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        #得到html 的全部內容
        print 121`"12312333333333333333333333333333333333333333333333333"
        return response.read()

"""
if __name__=='__main__':
	hd=HtmlDownload()
	url1='http://cuiqingcai.com'
	url2='https://baike.baidu.com/'
	html1=hd.download(url1)
	html2=hd.download(url2)
	#print (html2)
"""