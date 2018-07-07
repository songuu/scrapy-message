# -*- coding: utf-8 -*-
#from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors
import codecs
import json
from logging import log
from suse.dbhelper import *
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('info.json', 'w',encoding='utf8')#保存为json文件
    def process_item(self, item, spider):
    	for i in item.fields:
        	self.file.write(str(item[i])+'\n')
    def spider_closed(self, spider):#爬虫结束时关闭文件
        self.file.close()
class suseScrapyPipeline(object):
	def __init__(self,):
		pass
	def process_item(self,item,spider):
		testDBHelper=DBHelper()
		link=testDBHelper.connectDatabase()
		if link:
			with link as cursor:
				try:
					sql="insert into suse_info values(%s,%s,%s,%s,%s,%s)"
					params=(item["course_id"],item["course_name"],item["course_time"],item["course_type"],item["course_position"],item["course_teacher"])
					cursor.execute(sql,params)
				except:
					print ('添加错误')
		else:
			print ('error')
		return item
		
'''class suseScrapyPipeline(object):
    def __init__(self,dbpool):
        self.dbpool=dbpool
        self.dbpool=adbapi.ConnectionPool('pymysql',
                                          host='localhost',
                                          db='','''用户数据库'''
                                          user='','''用户数据库名'''
                                          passwd='','''用户数据库'''
                                          cursorclass=pymysql.cursors.DictCursor,
                                          charset='utf8',
                                          use_unicode=False)       
        
    @classmethod
    def from_settings(cls,settings):
        dbparams=dict(
            host=settings['MYSQL_HOST'],#读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',#编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool=adbapi.ConnectionPool('pymysql',**dbparams)#**表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        return cls(dbpool)#相当于dbpool付给了这个类，self中可以得到

    #pipeline默认调用
    def process_item(self, item, spider):
        query=self.dbpool.runInteraction(self._conditional_insert,item)#调用插入的方法
        query.addErrback(self._handle_error,item,spider)#调用异常处理方法
        return item
    
    #写入数据库中
    def _conditional_insert(self,tx,item):
        #print item['name']
        sql="insert into suse_info values(%s,%s,%s,%s,%s,%s)"
        params=(item["course_id"],item["course_name"],item["course_time"],item["course_type"],item["course_position"],item["course_teacher"])
        tx.execute(sql,params)
    
    #错误处理方法
    def _handle_error(self, failue, item, spider):
        print ('--------------database operation exception!!-----------------')
        print ('-------------------------------------------------------------')
        print (failue)'''
'''class SusePipeline(object):
    def process_item(self, item, spider):
		conn=pymysql.connection(
				host='localhost',
				user='','''数据库用户名'''
				password='','''用户密码'''
				db='','''用户自定义数据库'''
				charset='utf8',
				cursorclass=pymysql.cursors.DictCursor
			)
		with conn as cursor:
			v=(item['id'],item['name'],item['time'],item['teacher'],item['position'],item['type'])
			sql='insert into suse_info (id,name,time,teacher,position,type) values (%s,%s,%s,%s,%s,%s)'
			try:
				cursor.excute(sql,v)
			except Exception as e:
				print (e)
			finally:
				print ('完成')
				conn.commit()
				cursor.close()'''