'''
integrity.html
'''

from get_html_source import get_html
import re, bz2, chardet

'''
Where is the missing link?
'''

url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
A = get_html(url)

with open('source.txt', 'wt') as f:
    content = A.get_req()
    m = re.findall('href="(.+?)"', content)
    m2 = re.findall('un: (.+?)\n', content)
    m3 = re.findall('pw: (.+?)\n', content)
    f.write(m[1][2:] + '\n')
    f.write(m2[0].replace('\'','') + '\n')
    f.write(m3[0].replace('\'','') + '\n')
    f.write('un: ' + str(bz2.decompress(\
        b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')\
        .decode('utf-8')) + '\n')
    f.write('pw: ' + str(bz2.decompress(\
        b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')\
        .decode('utf-8')))   

'''
/return/good.html
BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084
BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08

Resolution site: http://www.pythonchallenge.com/pc/return/good.html
BZh91AY&SY: Header of bz2 file
Value after 'BZh91AY&SY': Binary value compressed with bz2

un: huge
pw: file
'''