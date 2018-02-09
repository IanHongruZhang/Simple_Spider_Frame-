# -*- coding: utf-8 -*-

import threading
import queue
import time
import os
from config import *
from log_format import logger
import inspect
import tools

# work_threading count
fifo = FIFO

if fifo:
	work_queue = queue.Queue()
	save_queue = queue.Queue()
	url_content_queue = queue.Queue()

else:
	work_queue = queue.LifoQueue()
	save_queue = queue.LifoQueue()
	url_content_queue = queue.LifoQueue()

def get_work_queue():
	'''
	working queue
	''' 
	while 1:
		if not work_queue.empty():
			# every item in queue is a dict
			_dict = work_queue.get()

			if not isinstance(_dict,dict):
				msg = 'put queue data is not dict,please check'
				raise ValueError(msg)
	        _args = _dict.get("args")
	        work_func = _dict.get("work_func")
	        dont_filter = _dict.get("dont_filter")

	        if content is not None:
	        	if content == 'HAS CRAWLED':
	        		logger.warning("%s has crawled" % url)
	        	else:
	        		_dict["content"] = content
	        		_dict["url"] = url

	        		follow_func = _dict.get('follow_func')
	        		save_func =_dict.get("save_func")

	        		if follow_func:
	        			handle_thread_exception(follow_func)
	        		if save_func:
	        			save_queue.put(_dict)
	        work_queue.task_done()

def get_save_queue():
    '''
	saving queue
	'''
	while 1:
		if not save_queue.empty():
			_dict = save_queue.get()
			save_func = _dict.get("save_func")
			handle_thread_exception(save_func,_dict)
			save_queue.task_done()

def start(thread_num = thread_num):
	for i in range(thread_num):
		get_work_thread = threading.Thread(target = get_work_queue)
		saving_threading_list.append(get_work_thread)
		get_work_thread.setDaemon(True)
		get_work_thread.start()

	for i in range(thread_num * 2):
		get_save_thread = threading.Thread(target = get_save_queue)
		save_threading_list.append(get_save_thread)
		get_save_thread.setDaemon(True)
		get_save_thread.start()

	show_size_thread = threading.Thread(target = show_size)
	show_size_thread.setDaemon(True)
	show_size_thread.start()

def handle_thread_exception(func,_dict):
	try:
		func(_dict)
	except Exception as e:
		msg = 'ERROR INFO in {func}:{e}'.format(func = func,e=e)
        logger.error(tools.format_error_msg(inspect.stack()[1][1],inspect.stack()[1][3],msg))

def show_size():
	while 1:
		 if not work_queue.empty() or not save_queue.empty():
            msg = 'AT %s ,work queue size is [%d]' % (time.strftime('%Y-%m-%d %H:%M:%S'), work_queue.qsize())
            logger.info(msg)

            msg = 'AT %s ,save queue size is [%d]' % (time.strftime('%Y-%m-%d %H:%M:%S'), save_queue.qsize())
            logger.info(msg)

            msg = 'work threading total count is [%d], active count is [%d]' % (
                len(work_threading_list), tools.isThreadAlive(work_threading_list))
            logger.info(msg)

            msg = 'save threading total count is [%d], active count is [%d]' % (
                len(save_threading_list), tools.isThreadAlive(save_threading_list))
            logger.info(msg)

            time.sleep(2)


