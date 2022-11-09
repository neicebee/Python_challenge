'''
channel.html
'''

import re, zipfile
from get_html_source import get_html

url = "http://www.pythonchallenge.com/pc/def/channel.html"
A = get_html(url)

with open('source.txt', 'wt') as f:
    source = A.get_req().replace('\n', '')
    m = re.findall('<!--(.+?)-->', source)
    for i in m:
        f.write(i.strip()+'\n')

'''
<-- zip

The following has nothing to do with the riddle itself. 
I just thought it would be the right point to offer you to donate to thePython Challenge project. 
Any amount will be greatly appreciated.
-thesamet
'''

url = url.replace('html', 'zip')
A.change_url(url)

with open('channel.zip', 'wb') as f:
    f.write(A.get_content())

with open('channel/readme.txt', 'rt') as f:
    msg = f.read().replace('\n', '')
    num = re.findall('(\d{5})', msg)[0]
    print(num)

'''
welcome to my zipped list.

hint1: start from 90052
hint2: answer is inside the zip
'''

ZF = zipfile.ZipFile('channel.zip')

while num:
    FILE = f'channel/{num}.txt'
    with open(FILE, 'rt') as f:
        txt = f.read()
        num = ''.join(re.findall('(\d+?)', txt))
        if not num:
            '''
            Collect the comments.
            '''
            break
        print(ZF.getinfo(FILE.replace('channel/', '')).comment.decode('UTF-8'), end='')
        '''
        extract comments from zip file => getinfo('file_name').comment
        '''