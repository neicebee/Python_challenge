![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2Fz2tmp%2FbtqzZ2oVzu5%2FtZPTijNWXmFDs11oFDd0X0%2Fimg.png)

http://pythonchallenge.com

# Python Challenge 7 풀이

## Explanation

### Secret Info Website

```python
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
```
- **_해당 이미지를 작업 디렉터리에 넣는 코드_**
- 딱히 웹페이지에서 얻을 힌트는 없음
- 페이지 중간의 사진을 보면 색깔이 나열된 띠가 있음
- 사진의 픽셀을 분석해야 하는 문제 같음 => PIL module
  - PIL module은 `pip install PIL` 이 아닌 `pip install pillow` 로 패키지를 다운받아야 함

### Solution Process 1

```python
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
```
- Image 객체의 size 메서드는 너비와 높이 순으로 Tuple을 반환함
- White to Black 색깔의 특징은 RGB 값이 모두 같음
- 해당 이미지의 1열에 해당하는 RGB 값을 뽑아보면 43~51행이 같은 RGB 값을 갖고 있음
- 이미지 높이의 중간에 해당하는 47행을 기본값으로 설정하고 진행

### Solution Process 2

```python
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
```
- 47행의 모든 열을 살펴보면 동일한 값이 7번 반복되는 것을 알 수 있음
- 그리고 동일한 값이 128을 넘지 않음으로 보아 해당 값을 ASCII 코드값으로 변경할 수 있어 보임

### Solution Process 3

```python
    except_row = [x for x in range(width) if len(set(img.getpixel((x, height//2))))>2][0]
    '''
    From 608 row, the pixel value of the real image => except 608 row ~
    '''
```
- 분석 중인 이미지를 보면 끝자리에 띠가 끊겨있고 진짜 이미지가 있는 것이 보임
- 해당 행을 찾기 위한 코드

### Solution Process 4

```python
    msg = ''
    for x in range(0, except_row, 7):
        msg += chr(img.getpixel((x, height//2))[0])
    '''
    smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
    '''
```
- 이미지 내 띠의 RGB 값을 ASCII로 변환함
- smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
  - 다음 레벨로 갈 수 있는 단어도 ASCII로 변환해야 할 것으로 보임

### Solution Process 5

```python
    m = re.findall('[0-9]{3}', msg)
    print(''.join((chr(int(c)) for c in m)))

    '''
    integrity
    '''
```
- 해당 메시지의 숫자 값을 정규표현식으로 처리하여 한 번에 정답이 나오도록 코딩

## Answer

URL 정답값: **integrity**