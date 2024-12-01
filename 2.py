'''
ocr.html
'''

'''
recognize the characters. maybe they are in the book,
but MAYBE they are in the page source.
'''

# import re
# from get_html_source import get_html

# A = get_html('http://www.pythonchallenge.com/pc/def/ocr.html')

# html = A.get_req().replace('\n', '')

# m = re.findall('<!--(.+?)-->', html)

# if m:
#     with open('source.txt', 'wt') as f:
#         f.write(m[1])

# '''
# m[0] = find rare characters in the mess below:
# '''

# with open('source.txt', 'rt') as f:
#     below = f.read()
#     characters = ''.join(re.findall('[a-zA-Z]', below))
#     print(characters)

import re
from get_html_source import get_html

A = get_html('http://www.pythonchallenge.com/pc/def/ocr.html')

html = A.get_req().replace('\n', '')
m = re.findall('<!--(.+?)-->', html)
msg = ''.join(re.findall('[a-zA-Z]', m[1]))
print(msg)