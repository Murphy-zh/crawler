# coding=utf-8
import re
import time
import datetime
from random import randint
from dateutil.parser import parse
from loguru import logger
from pathlib import Path


logpath = Path(__file__).parent.parent / 'logs'

def get_logger(name):
    file_name = Path(name).name.split(".")[0]
    sink = "{}.log".format(logpath / file_name)
    logger.add(
        sink=sink,
        encoding="utf8",
        format="{time:YYYY-MM-DD HH:mm:ss} >>> {message} | func:{function} - {level}",
        rotation='5MB'
    )
    return logger

def format_time(old_time,fmt_pattern=None):
    """
    格式化时间
    """
    # 时间戳
    if isinstance(old_time,int):
        d = datetime.datetime.fromtimestamp(old_time)
        return d.strftime(fmt_pattern if fmt_pattern else '%Y-%m-%d %H:%M:%S')

    # 其他时间类型 "Fri Jul 09 04:41:55 +0000 2021":"%a %b %d %H:%M:%S +0000 %Y"
    try:
        d = parse(old_time)
        # if d.hour==d.minute==d.second==0:
        return d.strftime(fmt_pattern if fmt_pattern else '%Y-%m-%d %H:%M:%S')
    except Exception:
        date_f = re.search('(?P<year>\d+)[-/年](?P<month>\d+)[-/月](?P<day>\d+)[-/日]?.?(?P<hour>\d+)?[-:/时]?(?P<minute>\d+)?[-:/分]?(?P<second>\d+)?[-:/秒]?',old_time)
        if date_f:
            year,month,day = date_f.group("year"),date_f.group("month").zfill(2),date_f.group("day").zfill(2)
            hour, minute, second = date_f.group('hour'), date_f.group('minute'), date_f.group('second')
            if len(year)==2:
                year = "20" + year
            
            if hour:
                if not minute:
                    minute = str(randint(0, 59))
                if not second:
                    second = str(randint(0,59))
                return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second
            else:
                hour = str(randint(0, 23))
                minute = str(randint(0, 59))
                second = str(randint(0,59))
                return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second

def time_use(func):
    def decorator(*args,**kwargs):
        start = time.time()
        results = func(*args, **kwargs)
        time_use = time.time() - start
        return results,time_use
    return decorator

if __name__ == "__main__":
    # a = "Fri Jul 09 04:41:55 +0000 2021"
    a = "2008-09-26"
    print(format_time(a))


    # time_tmp = time.strptime(a,"%a %b %d %H:%M:%S +0000 %Y")

    # time_new = time.strftime("%Y-%m-%d %H:%M:%S",time_tmp)
    # print(time_new)

