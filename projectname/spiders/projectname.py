# -*- coding: utf-8 -*-
import scrapy
from PIL import Image
from scrapy import Request,FormRequest
import re
from suse.items import suse_course_Item


class suse(scrapy.Spider):
	name=''    '''爬虫名字  很重要'''
	start_urls=[''] '''学校官网'''
	captcha_path=''   '''验证码信息'''
	headers={
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
	}
	Username=''   '''在校注册用户名'''
	Password=''   '''用户密码'''
	def parse(self,response):
		captcha_url=''   '''验证码页面'''
		yield Request(url=captcha_url,headers=self.headers,callback=self.parse_captcha)
	def parse_captcha(self,response):
		with open(self.captcha_path,'wb') as f:
			f.write(response.body)
			f.close()
		im=Image.open(self.captcha_path)
		im.show()
		im.close()
		captcha=input('input the captcha:\n')
		yield Request(url='',callback=self.login,meta={'txtSecretCode':captcha})
	def login(self,response):
		login_url=''
		yield FormRequest( '''自己登陆官网查看学校网站信息'''
				url=login_url,
				method='POST',
				formdata={
					'__VIEWSTATE':'',
					'txtUserName':self.Username,
					'TextBox2':self.Password,
					'txtSecretCode':response.meta['txtSecretCode'],
					'RadioButtonList1':'',
					'Button1':'',
					'lbLanguage':'',
					'hidPdrs':'',
					'hidsc':'',
				},
				callback=self.after_login,
			)
	def after_login(self,response):
		course_href=response.xpath('//ul[@class="nav"]/li[6]/ul/li[2]/a/@href').extract_first()
		full_course_url = response.urljoin(course_href)
		chose_href=response.xpath('//ul[@class="nav"]/li[2]/ul/li/a/@href').extract_first()
		full_chose_url=response.urljoin(chose_href)
		yield Request(url=full_course_url,callback=self.course_form)
		yield Request(url=full_course_url,callback=self.chose_form)
	def chose_form(self,response):
		chose_num=response.xpath('//span[@id="Label4"]').extract_first()
		
	def course_form(self,response):
		course=response.xpath('//*[@id="Table1"]').extract()
		course_td=[]
		m=[]
		course_name=[]
		course_info=[]
		for course_tr in course:
			for i in course_tr.split('</tr>'):
				course_td.append(i+'</tr>')
		for j in course_td:
			for i in j.split('</td>'):
				m.append(i.split('<br>'))
		for i in m[2:-3]:
			i[0]=i[0].replace(i[0],i[0].split('>')[1])
			if len(i) <5:
				del i
			else:
				course_name.append(i)
		for name in course_name:
			if len(name)==11:
				course_info.append(name[0:5])
				course_info.append(name[6:11])
			else:
				course_info.append(name)
		i=0
		item=suse_course_Item()
		for courses in course_info:
			item['course_name']=courses[0]
			item['course_time']=courses[2]
			item['course_type']=courses[1]
			item['course_position']=courses[4]
			item['course_teacher']=courses[3]
			item['course_id']=i
			i+=1
			print (item['course_name'])
			yield item
			

		



	
		