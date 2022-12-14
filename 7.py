'''
oxygen.html
'''

import re
from PIL import Image
from get_html_source import get_html

# url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
# A = get_html(url)

# with open('oxygen.png', 'wb') as f:
#     f.write(A.get_content())
'''
save image to working directory
'''

with Image.open('oxygen.png', 'r') as img:
    width, height = img.size
    
    # with open('source.txt', 'wt') as f:
    #     for y in range(height):
    #         f.write(f'{y} {img.getpixel((0, y))}\n')
    '''
    characteristics of white to black: Same R,G,B values

    43 (115, 115, 115, 255)
    44 (115, 115, 115, 255)
    45 (115, 115, 115, 255)
    46 (115, 115, 115, 255)
    47 (115, 115, 115, 255)
    48 (115, 115, 115, 255)
    49 (115, 115, 115, 255)
    50 (115, 115, 115, 255)
    51 (115, 115, 115, 255)
    
    rows 43 ~ 51 are the same
    height//2 == 47
    '''

    # with open('source.txt', 'wt') as f:
    #     for x in range(width):
    #         f.write(f'{x} {img.getpixel((x, height//2))}\n')
    '''
    0 (115, 115, 115, 255)
    1 (115, 115, 115, 255)
    2 (115, 115, 115, 255)
    3 (115, 115, 115, 255)
    4 (115, 115, 115, 255)
    5 (109, 109, 109, 255)
    6 (109, 109, 109, 255)
    7 (109, 109, 109, 255)
    8 (109, 109, 109, 255)
    9 (109, 109, 109, 255)
    10 (109, 109, 109, 255)
    11 (109, 109, 109, 255)
    12 (97, 97, 97, 255)
    ...
    606 (93, 93, 93, 255)
    607 (93, 93, 93, 255)
    608 (114, 112, 71, 255)
    609 (112, 110, 69, 255)
    628 (99, 85, 46, 255)

    Repeat the same value 7 times
    Values don't exceed 128(max of ASCII code) => Value can be changed to ASCII code
    '''

    except_row = [x for x in range(width) if len(set(img.getpixel((x, height//2))))>2][0]
    '''
    From 608 row, the pixel value of the real image => except 608 row ~
    '''

    msg = ''
    for x in range(0, except_row, 7):
        msg += chr(img.getpixel((x, height//2))[0])
    '''
    smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
    '''

    m = re.findall('[0-9]{3}', msg)
    print(''.join((chr(int(c)) for c in m)))

    '''
    integrity
    '''