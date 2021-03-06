---
layout: post
category: python
tag: [기초, TIL, codecademy]
title: 코데카데미 파이썬 기초과정 요약 - 문자열
---
## 문자열 Strings and Conditionals

* 문자열의 길이를 구하는 함수를 만들어보자
    ``` python
    def get_length(string):
        counter = 0
        for i in string:
            counter += 1
        print(counter)

    get_length("Luna")
    #결과
    4
    ```

* 해당 알파벳이 단어에 들어있는지 확인하는 함수를 만들어보자
    ``` python
    def letter_check(word, letter):
        for char in word:
            if char == letter:
                return True
        return False
    ```

* 작은 문자열이 큰 문자열 안에 포함되어있는지 알아보자 
    ``` python 
    def contains(big_string, little_string)
        return little_string in big_string
    ```
    편리한 'in' 을 사용하여 contain(포함)이라는 함수를 만들 수 있다.
    예를 들어 "a" in "Banana" 하면 True가 반환된다.

    ``` python
    def common_letters(string_one, string_two)
        common = []
        for letter in string_one:
        #string_one에 있는 모든 문자들 중에서 
            if (letter in string_two) and not (letter in common):
            #string_two에 있고, 이미 common에 들어있지 않은 문자라면 
                common.append(letter)
                #common에 추가한다.
        return common
    ```

## String 복습

* 유저이름을 이용해서 비밀번호를 만들어보자. 예를 들어 AbeSimp -> pAbeSim

    ``` python
    def password_gen(user_name):
        password=""
        for i in range(0, len(user_name)):
            password += username[i-1]
        return password
    ```

    답안에서 i-1을 사용한 부분이 인상깊었다.
    username[-1] username[0] username[1].. 이렇게 차곡차곡 쌓인다고 생각하면 된다.

* Split은 문자열을 리스트로 만들어준다. 반대로 join은 리스트를 문자로 만들어준다.

    ``` python
    authors = ["Audre Lorde", "An Qi", "Kamala Suraiya"]
    author_last_names=[]
    for name in authors:
        author_last_names.append(name.split()[-1])
    #결과
    ["Lorde","Qi","Suraiya"]
    ```

    예시1
    ``` python
    my_jusik = ["naver daum"]
    my_jusik.split(' ') = ["naver", "daum"]
    ```

    예시2
    ``` python
    daily_sales = ['유영 + $10 + white + 09/15/17', '수민 + $7 + blue + 09/15/17' ...]
    for transaction in daily_sales:
        daily_sales_split.append(transaction.split('+'))
    print(daily_sales_split)
    #결과
    [['유영','$10','white','09/15/17'],['수민','$7','blue','09/15/17]...]]
    ```

* Strip은 빈공간을 정리하거나 특정문자를 지워준다. 

    ``` python
    txt = "     banana     "
    x = txt.strip()
    print("of all fruits", x, "is my favorite")
    ```
    이외에 
    * replace() 교체한다. 
    * find() 해당 문자열의 위치를 찾는다.
    * format() 보간(interpolate{})해준다.
    등이 있다.

* 복습과제 : 시이름, 시인, 년도 순서로 되어있는 딕셔너리에서 각각을 분리하여 새 리스트에 넣어주고 이를 활용해서 문장을 출력해보자.

    ``` python
    highlighted_poems_details = [['Afterimages', 'Andre Lorde', '1997'],['The Shadow','William','1915']]
    titles = []
    poets = []
    dates = []
    for poem in highlighted_poems_details:
        title.append(poem[0])
        poets.append(poem[1])
        dates.append(poem[2])

    for i in range(0, len(highlighted_poems_details)):
        print('The poem {} was published by {} in {}'.format(titles[i],poets[i],dates[i]))
    ```