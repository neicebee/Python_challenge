'''
equality.html
'''

'''
One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
'''

import re
from get_html_source import get_html

A = get_html(url="http://www.pythonchallenge.com/pc/def/equality.html")

with open('source.txt', 'wt') as f:
    txt = A.get_req().replace('\n', '')
    m = re.findall("<!--(.+?)-->", txt)
    f.write(m[0])

with open('source.txt', 'rt') as f:
    msg = f.read()
    m2 = re.findall("[a-z]+[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]+", msg)
    print(''.join(m2))