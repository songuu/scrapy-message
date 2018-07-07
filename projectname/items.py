# -*- coding: utf-8 -*-


import scrapy
class suseItem(scrapy.Item):
	pass
		

class suse_course_Item(scrapy.Item):
	course_name=scrapy.Field()
	course_time=scrapy.Field()
	course_teacher=scrapy.Field()
	course_position=scrapy.Field()
	course_type=scrapy.Field()
	course_id=scrapy.Field()
