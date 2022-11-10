'''
oxygen.html
'''

from PIL import Image
from get_html_source import get_html

# url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
# A = get_html(url)

# with open('oxygen.png', 'wb') as f:
#     f.write(A.get_content())

with Image.open('oxygen.png', 'r') as img:
    width, height = img.size
    
    # with open('source.txt', 'wt') as f:
    #     for y in range(height):
    #         f.write(f'{y} {img.getpixel((0, y))}\n')
    '''
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

    with open('source.txt', 'wt') as f:
        for x in range(width):
            f.write(f'{x} {img.getpixel((x, 47))}\n')