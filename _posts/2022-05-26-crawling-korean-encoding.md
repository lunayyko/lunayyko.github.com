---
layout: post
category: backend
tag: [backend]
title: 파이썬 크롤링시 한글 깨짐
---

## 목적

사용자가 게시판에 링크 입력 시  뉴스 페이지에서 제목과 썸네일 등을 끌어오는데 한글 깨짐을 예방한다.

### 데이터 엔코딩을 덮어씌운다

```python

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers, timeout=3)

if data.encoding not in ['euc-kr', 'utf-8']:
    data.encoding = 'EUC-KR'

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select_one('meta[property="og:title"]')
image = soup.select_one('meta[property="og:image"]')
desc = soup.select_one('meta[property="og:description"]')

```

### 시행착오의 흔적

```python

charset = soup.select_one('meta[http-equiv="Content-Type"]')
print('charset', charset)

charset2 = charset.attrs("charset")
print('charset2', charset2)

# charset.get('content')[charset.get('content').find("charset="):]

charset3 = charset.get('content')[charset.get('content').find("charset="):].replace('charset=', '')
print('charset3', charset3)

charset4 = soup.headers.get_content_charset()
print('charset4', charset4)

# res = req.urlopen(url).read().decode(req.urlopen(url).headers.get_content_charset())
# req.urlopen(url).headers.get_content_charset()

# soup = BeautifulSoup(data.content.decode('utf-8', 'replace'), 'html.parser')


```