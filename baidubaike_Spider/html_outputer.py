# coding:utf-8
class HtmlOutputer(object):
	def __init__(self):
		self.datas=[]

	def collect_data(self,data):
		if data is None:
			return 
		self.datas.append(data)


	def output_html(self):
		print ('write in file ')
		fout=open('output.txt','w',encoding='utf-8')
		for data in self.datas:
			fout.write('url >> ')
			fout.write(data['url'])
			fout.write('title >> ')
			fout.write(data['title'])
			fout.write('summary >> ')
			fout.write(data['summary'])
		fout.close()
