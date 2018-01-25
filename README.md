# A simple spider frame:简单爬虫框架

config.py : 一些分离出的参数

data_save.py : 数据库端

html_parser.py : 解析端
目前有的工具:path,re,json，还要加bs4

log_format.py：日志格式化工具

page_downloader.py: 网页获取处理端，主逻辑是用requests.session.get()方法

UAS.py:头文件池
