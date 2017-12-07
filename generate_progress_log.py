#!/usr/bin/env python
# coding=utf-8

import time
import codecs

f = codecs.open('progress_log.txt', 'a+', 'utf-8')
time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
v = ['项目进度']
note = '准备好scrum表格'
result = time + '\t' + '-'.join(v) + '\t' + note + '\n'
f.writelines(result)
