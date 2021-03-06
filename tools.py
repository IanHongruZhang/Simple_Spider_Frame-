# -*- coding:utf-8 -*-
from log_format import logger
import inspect
import os

### Judging the threads status
def isThreadAlive(threads):
    count = 0
    for t in threads:
        if t.isAlive():
            count += 1
    return count

### formatting the error infos
def format_error_msg(file_name,func_name,error_msg):
    error_info = '''
    detail_error_info
    ##################
    file_name: {},
    func_name: {},
    error_msg: {}
    ##################
    '''.format(file_name, func_name, error_msg)
    return error_info

def format_put_data(args,work_func,dont_filter = False,follow_func = None,tag = None,need_save = True,save_func = None,meta = None):
    put_data = {'args':args,
                'work_func':work_func,
                'follow_func':follow_func,
                'dont_filter':dont_filter,
                'tag':tag,
                'need_save':need_save,
                'save_func':save_func,
                'meta':meta}

    if not isinstance(args,dict) or not args:
        msg = "IN [put_data],args has to be dict and can not be empty, please check, exiting......"
        logger.error(format_error_msg(inspect.stact()[1][1],inspect.stack()[1][1],inspect.stack()[1][3],msg))
        os._exit(0)

    elif 'url' not in args.keys():
        msg = 'IN [put_data], url has to be a key in args and can not be modified ,please check, exiting......'
        logger.error(format_error_msg(inspect.stack()[1][1], inspect.stack()[1][3], msg))
        os._exit(0)

    if meta and not isinstance(meta, dict):
        msg = 'meta has to be dict while you defined it ,please check, exiting......'
        logger.error(format_error_msg(inspect.stack()[1][1], inspect.stack()[1][3], msg))
        os._exit(0)

    # save_func
    if save_func and not callable(save_func):
        msg = 'IN [put_data], save has to be callable while you define it ,please check, exiting......'
        logger.error(format_error_msg(inspect.stack()[1][1], inspect.stack()[1][3], msg))
        os._exit(0)

    return put_data



