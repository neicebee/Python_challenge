'''
linkedlist.html
linkedlist.php
'''

import re
from get_html_source import get_html

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
A = get_html(url)

with open('source.txt', 'wt') as f:
    m = re.findall('<!--(.+?)-->', A.get_req().replace('\n', ''))
    nothing = ''.join(re.findall('[0-9]{5}', A.get_req().replace('\n', '')))
    f.write(''.join(m).strip())

'''
urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.

linkedlist.php?nothing=12345
and the next nothing is 44827
'''

while nothing:
    print(nothing)
    A.change_url(url+'?nothing='+nothing)
    source = A.get_req()

    if m2:=re.findall('[0-9]+?', source):
        if len(m2) > 5:
            nothing = ''.join(m2[5:])
            continue
        nothing = ''.join(m2)
        continue
    elif not m2 and "Divide" in source:
        print(source.strip())
        nothing = str(int(int(nothing)/2))
        continue
    
    print(source)
    nothing = None