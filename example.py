#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入模块

import sys
sys.path.append('/home/documents')

from spider.tools import format_put_data
from spider.data_save import pipeline
from spider.html_parser import parser
from spider.page_downloader import aispider
from spider.threads import start,work_queue,save_queue
from spider.log_format import logger

root_url_format = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_album.fcg?g_tk=676629472&loginUin=549411552&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&singermid={singermid}&order=time&begin={begin}&num={num}&exstatus=1"

class SpiderMain(object):
	def __init__(self):
		self.logger = logger
		self.downloader = aispider
		self.parser = parser 
		self.pipeline = pipeline
    
	def craw(self,singer_mids):
		for singer_mid in singer_mids:
			url = root_url_format.format(singermid = singer_mid,begin = begin,num = num)
			# use format_put_data
			put_data = format_put_data(args = {'url':url,'method':'get','submit_data':None},
				work_func = self.downloader.request,
				follow_func = self.get_total_num)
			work_queue.put(put_data)

	def get_total_num(self,response):
		# get content from request
		html_content = response.get('content')
		# using parse
		datas = parser.get_data_by_json(html_content)
		total_num = datas.get("data").get("total",'')
		