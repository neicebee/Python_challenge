'''
peak.html
'''

# import re, pickle
# from get_html_source import get_html

# url = "http://www.pythonchallenge.com/pc/def/peak.html"
# A = get_html(url)

# with open('source.txt', 'w+') as f:
#     source = A.get_req().replace('\n', '')
#     m = re.findall('<!--(.+?)-->', source)
#     m2 = re.findall('[a-z]{6}.p', source)
#     f.write(m[0].strip()+'\n'+m2[0].strip())
#     A.change_url(url.replace('peak.html', m2[0]))

# '''
# peak hell sounds familiar ?
# banner.p
# '''

# with open('banner.p', 'wt') as f:
#     f.write(A.get_req())

# with open('banner.p', 'rb') as f:
#     pfile = pickle.load(f)

# with open('source.txt', 'wt') as f:
#     for i in range(len(pfile)):
#         for j in range(len(pfile[i])):
#             f.write(pfile[i][j][0]*pfile[i][j][1])
#         f.write('\n')

import re, pickle
from get_html_source import get_html

A = get_html('http://www.pythonchallenge.com/pc/def/peak.html')

m = re.findall('[a-z]{6}.p', A.get_req())
A.change_url(A.check_url().replace('peak.html', m[0]))

with open('banner.p', 'wt') as f:
    f.write(A.get_req())

with open('banner.p', 'rb') as f:
    pf = pickle.load(f)
    
with open('result.txt', 'wt') as f:
    for i in range(len(pf)):
        for j in range(len(pf[i])):
            f.write(pf[i][j][0]*pf[i][j][1])
        f.write('\n')