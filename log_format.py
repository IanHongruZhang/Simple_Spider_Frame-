#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by shimeng on 17-8-10
import os
import time
import logging
from config import *
import shutil

def spider_log(log_name = spider_name,file_folder = log_folder_name,level = loggingINFO,delete_existed_log=delete_existed_logs):
	if os.path.exists(file_folder):
		if delete_existed_logs:
			shutil.rmtree(file_folder)
			os.mkdir(file_folder)
	else:
		os.mkdir(file_folder)

	create_time = time.shrftime('%Y-%m-%d %H-%M-%S')
	logger = logging.getLogger(log_name)

	logger.setLevel(level)

	file_handler = logging.FileHandler('[%(asctime)s] - %(filename)s - [line:%(lineno)d] - [%(levelname)s]: %(message)s')
	file_handler.setFormatter(formatter)
	stream_handler.setFormatter(formatter)

	logger.addHandler(file_handler)
	logger.addHandler(stream_handler)
	return logger

logger = spider_log(log_name = "test")

if __name__ == '__main__':
    logger = spider_log('log')
    logger.warning('warn message')
    logger.info('info message')
    logger.debug('debug message')