# -*- coding:utf-8 -*-

###解析网页！！！
###目前几种：xpath,re,json
###需要添加的解析方法：BeautifulSoup,urllib2,selenium

import re
import json
import lxml.html as H
from spider.log_format import logger
import inspect
from spider.tools import format_error_msg

class HtmlParser(object):
    '''
    re,xpath,json
    '''
    def __init__(self,):
        self.logger = logger

    # xpath
    # references:urls_xpath
    def get_data_by_xpath(self,html_page_source,urls_xpath):
        try:
            self.doc = H.document_transforming(html_page_source)
            # document_transforming方法：将文本格式的html变为html文件
            # 实际上是lxml的解析器进行解析
        except Exception as e:
            msg = "Error msg:%s in [get_data_by_xpath]" % e
            self.logger.error(format_error_msg(inspect.stack())[1][1],inspect.stack()[1][3],msg)
           #
        else:
            data = self.doc.xpath(urls_xpath)
            return data
    # re
    # pattern
    def get_data_by_re(self,html_page_source,pattern,flags=re.DOTALL):
        try:
            data = re.findall(pattern,html_page_source,flags = flags)
        except Exception as e:
            msg = "Error msg:%s in [get_data_by_re]" % e
            self.logger.error(format_error_msg(inspect.stack()[1][1],inspect.stack()[1][3],msg))
        else:
            return data

    def get_data_by_json(self,html_page_source):
        try:
            data = json.loads(html_page_source)
        except Exception as e:
            msg = "Error msg:%s in [get_data_by_json]" % e
            self.logger.error(format_error_msg(inspect.stack()[1][1], inspect.stack()[1][3], msg))

        else:
            return data

parser = HtmlParser()




