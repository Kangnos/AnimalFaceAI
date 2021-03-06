from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from pathlib import Path

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
people = {'puppy': ['강다니엘', '백현', '박보검', '송중기'],
          'cat': ['황민현', '시우민', '이종석', '강동원', '이종석', '이준기'],
          'bear': ['마동석', '조진웅', '조세호', '안재홍'],
          'dinosaur': ['윤두준', '이민기', '육성재', '공유', '김우빈']}
Path("./img").mkdir(parents=True, exist_ok=True) # img라는 디렉토리 생성
for k, v in people.items():
    Path("./img/" + k).mkdir(parents=True, exist_ok=True) # 디렉토리 생성 함수 여기서 k는 people list의 key의 값이다. v는 peop list의 value 값이다
    for person in v: # 뜻: v는 반복문에서 person이라는 변수로 사용하겠다 이소리
        url = baseUrl + quote_plus(person) # qutoe_plus는 문자열을 url 구문으로 바꿔주는 함수이다
        html = urlopen(url)
        soup = bs(html, "html.parser")
        img = soup.find_all(class_='_img', limit=45)
        Path("./img/" + k + '/' + person).mkdir(parents=True, exist_ok=True) # 디렉토리 생성 함수
        n = 1
        for i in img:
            imgUrl = i['data-source']
            with urlopen(imgUrl) as f:
                with open('./img/' + k + '/' + person + '/' + person + ' ' + str(n)+'.jpg','wb') as h: # w - write b - binary
                    img = f.read()
                    h.write(img)
            n += 1
print('다운로드 완료')
