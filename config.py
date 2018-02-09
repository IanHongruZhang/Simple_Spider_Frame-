# -*- coding: utf-8 -*-
## 参数设置段

spider_name = 'qq_music_spider'

## 
log_folder_name = '%s_logs' % spider_name
dele_existed_log = True

## 一些参数的设置
thread_num = 30 ### 爬虫线程数
sleep_time = 1 ### 爬虫休息时间
retry_times = 10 ### 报错重试次数
time_out = 5 ### 短线隔离时间
use_proxy = False ### 使不使用代理
ip = None ###

## 请求移动端的user-agent还是pc端的header
ua_type = 'pc'
## header在UAS.py中

## 队列顺序
FIFO = 0

## 是否使用自定义的header
diy_header = None

header = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Referer': 'https://y.qq.com/n/yqq/song/003OUlho2HcRHC.html',
}

###
diy_header = None

## 定义状态码
status_code = [200,304,404]

## 数据库段设置（此次用mongodb)
connect = False
host = 'yours'
port = 27017
database_name = 'yours'