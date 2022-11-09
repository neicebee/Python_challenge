![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2Fz2tmp%2FbtqzZ2oVzu5%2FtZPTijNWXmFDs11oFDd0X0%2Fimg.png)

http://pythonchallenge.com

# Python Challenge 6 풀이

## Explanation

### Secret Info Website

```python
import re, zipfile
from get_html_source import get_html

url = "http://www.pythonchallenge.com/pc/def/channel.html"
A = get_html(url)

with open('source.txt', 'wt') as f:
    source = A.get_req().replace('\n', '')
    m = re.findall('<!--(.+?)-->', source)
    for i in m:
        f.write(i.strip()+'\n')
```
- 웹페이지 소스에서 주석 뽑기

1. <-- zip

2. The following has nothing to do with the riddle itself. 
I just thought it would be the right point to offer you to donate to the Python Challenge project. 
Any amount will be greatly appreciated. **_-thesamet_**
   - 다음은 수수께끼 그 자체와 관련이 없다. 나는 그저 당신이 파이썬 챌린지 프로젝트에 기부함을 제안하는 것이 올바른 점이라고 생각했다. 얼마의 금액이든 대단히 감사하겠다.

### Solution Process 1

- `zip` 이라는 단어가 제시되었음
- 해당 문제의 링크에서 `channel.zip` 으로 바꾸면 zip 파일이 다운로드됨

```python
url = url.replace('html', 'zip')
A.change_url(url)

with open('channel.zip', 'wb') as f:
    f.write(A.get_content())
```
- 링크 재설정 후 콘텐츠 다운로드
- 해당 파일 이름을 설정 후 `byte` 형식으로 열어 `get_content()` 를 호출해 덮어씌워주면 스크립트로 파일을 다운로드 받을 수 있음

### Solution Process 2

- zip 파일 내의 `readme.txt` 를 읽고 이어나가보자

```python
with open('channel/readme.txt', 'rt') as f:
    msg = f.read().replace('\n', '')
    num = re.findall('(\d{5})', msg)[0]
    print(num)
```
- welcome to my zipped list.
- hint1: start from 90052
  - {해당 번호}.txt 파일 내에 다음으로 갈 파일 번호가 적혀있어 처음 들를 파일 변수를 지정하기 위해 정규표현식으로 `90052`를 추출해내었음
- hint2: answer is inside the zip
  - 답변은 zip 내에 있다고 함

### Solution Process 3

- txt 파일 내의 루트를 while 문으로 돌려 답변을 찾아내보자
  
```python
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
```

- 돌리다보면 마지막에서 해당 파일 번호가 아닌 `Collect the comments.` 라는 문장이 적혀있는 파일이 나옴
- zip 파일에는 comment라는 칸이 있음
- 해당 comment는 zipfile 객체의 getinfo().comment 메서드로 추출해낼 수 있음

```
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
```

### Solution Process 4

- http://www.pythonchallenge.com/pc/def/hockey.html 접속
- 페이지에 `it's in the air. look at the letters.` 라는 문구가 있음
- 큰 문자가 아닌 큰 문자를 만든 문자를 보면 `OXYGEN (산소)` 즉, 정답은 oxygen

## Answer

URL 정답값: **oxygen**