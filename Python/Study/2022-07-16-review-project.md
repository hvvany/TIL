

# Python 프로젝트 코드리뷰



---

## 00. 텍스트 데이터 출력 (연습)

- 아래의 내용을  `00.txt`에 기록하시오.

### 결과 예시

```
N회차 홍길동
Hello, Python!
1일차 파이썬 공부 중
2일차 파이썬 공부 중
3일차 파이썬 공부 중
4일차 파이썬 공부 중
5일차 파이썬 공부 중
```

---

### 내가  작성한 코드

```python
with open('00.txt', 'w', encoding='utf-8') as f:
    f.write('3회차 김준환\n')
    f.write('Hello, Python!\n')
    for i in range(5):
        f.write(f'{i}일차 파이썬 공부 중\n')
```



---

## 01. 텍스트 데이터 입력 (연습)

- 과일 데이터 

  ```fruits.txt```를 활용하여 총 과일의 갯수를 ```01.txt```  에 기록하시오.

  - 과일은 하나당 한 줄에 기록되어 있습니다.

### 결과 예시

```
394
```

### 내가 작성한 코드

```python
with open('data/fruits.txt','r', encoding='utf-8') as f:
    cont = f.readlines()
    print(str(len(cont)))
with open('01.txt', 'w', encoding='utf-8')as f:
    f.write(str(len(cont)))
    
    # readline으로 구현시 문자열로 가져오는데 이때 짝수번만 가져오더라
    # for 문으로 구현 했는데 readlines를 for에서 쓰니 이유는 모르겠지만 첫 문장은 뛰어 넘더라 그래서 그냥 바로 길이를 구해서 출력
```

### 다른 전공자 예시

```python
with open('data\\fruits.txt') as f:
    fruit_list = f.readlines()
    print(len(fruit_list))
```

> readlilne은 문자열로 가져옴
>
> readlines는 리스트로 담아서 가져옴
>
> 파일을 불러와서 열때는 with open('이름', '모드', 인코딩) as 변수 이름   으로 연다.



---

## 02. 텍스트 데이터 활용 - 특정 단어 추출

- 과일 데이터 

  ```fruits.txt```를 활용하여 ```berry```로 끝나는 과일의 갯수와 목록을 ```02.txt``` 에 기록하시오.

  - 과일은 하나당 한 줄에 기록되어 있습니다.

### 결과 예시

**순서는 달라도 됩니다.**

```
18
Honeyberry
Blackberry
Gooseberry
Juniper berry
Cranberry
Salal berry
Goji berry
Salmonberry
Bilberry
Cloudberry
Huckleberry
Raspberry
Mulberry
Elderberry
Marionberry
Strawberry
Boysenberry
Blueberry
```

### 내가 작성한 코드

```python
count = 0
strip_lst = []
berry_lst = []

with open('data/fruits.txt','r', encoding='utf-8') as f:
    full_data = f.readlines()
    for berry in full_data:
        strip_lst.append(berry.rstrip())
    for text in strip_lst:
        if text[-5:] == 'berry' and text not in berry_lst:
            print(text)
            berry_lst.append(text)   # 새 값만 추가하여 중복 제거
            count += 1
    print(count)
    #print(berry_lst)

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(str(count)+'\n')
    for berry in berry_lst:
        f.write(berry+'\n')
```

### 다른 전공자 예시

```python
fruit_list = []

with open('data\\fruits.txt', 'r') as f:
    lines = f.readlines()
    fruit_list = list(map(lambda s: s.strip(), lines))

fruit_berry = [fruit for fruit in fruit_list if fruit.endswith('berry')]   # endswith메소드 사용
fruit_berry = set(list(fruit_berry))   # set 사용하여 중복 제거

with open('02.txt', 'w') as f1:
    f1.write(str(len(fruit_berry))+'\n')
    for fruit in fruit_berry:
        f1.write(fruit+'\n')
```

> 첫 글자 포함여부 .startswith('단어')
>
> 마지막 글자 포함여부 .endswith('단어')
>
> set{1,2,3,2,1} -> {1,2,3}  순서 없이 중복 제거하여 저장하는 데이터 형태



---

## 03. 텍스트 데이터 활용 - 등장 횟수

- 과일 데이터 `fruits.txt`를 활용하여 과일의 이름과 등장 횟수를  `03.txt` 에 기록하시오.

### 결과 예시

**순서는 달라도 됩니다.**

```
Boysenberry 3
Blueberry 4
Avocado 1
Marionberry 3
Date 9
...
Melon 1
berryfake 1
```

### 내가 작성한 코드

```python
strip_lst = []
fruit_dic = {}
with open('data/fruits.txt','r', encoding='utf-8') as f:
    full_data = f.readlines()
    for text in full_data:
        strip_lst.append(text.rstrip()) 
    for fruit in strip_lst:
        if fruit not in fruit_dic:
            fruit_dic[fruit] = 1
        else:
            fruit_dic[fruit] += 1
with open('03.txt', 'w', encoding='utf-8')as f:
    for name in fruit_dic:
        k = name
        v = fruit_dic[name]
        f.write(str(k)+' '+str(v)+'\n')
```

### 다른 전공자 예시

```python
fruit_list = []
fruit_dict = {}

with open('data\\fruits.txt', 'r') as f:
    lines = f.readlines()

fruit_list = list(map(lambda s: s.strip(), lines))
    
for fruit_list_element in fruit_list:
    fruit_dict[fruit_list_element] = fruit_dict.get(fruit_list_element, 0) + 1

with open('03.txt', 'w') as f1:
    for k, v in fruit_dict.items():        # .items 를 사용하여 바로 key value 변수 생성
        f1.writelines([k, " ", str(v), '\n'])
```

> 첫 글자 포함여부 .startswith('단어')
>
> 마지막 글자 포함여부 .endswith('단어')
>
> set{1,2,3,2,1} -> {1,2,3}  순서 없이 중복 제거하여 저장하는 데이터 형태



---

## 04. JSON 데이터 활용 - 영화 단일 정보

- 영화 데이터 ```movie.json``` 을 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.
  - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
  - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.
- `id`, `title`, `vote_average`, `overview`, `genre_ids`으로 구성된 결과를 만듭니다. **(결과 예시 참고)**

### 결과 예시

```json
{'genre_ids': [18, 80],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```

### 내가 작성한 코드

```python
import json
from pprint import pprint


def movie_info(movie):
    pass
	# 여기서 부터 코드 작성
    f = open('data/movie.json', 'r', encoding='utf-8')
    mv = json.load(f)
    result = {
        'id' : mv.get('id'),
        'title' : mv.get('title'),
        'vote_average' : mv.get('vote_average'),
        'overview' : mv.get('overview'),
        'genre_ids' : mv.get('genre_ids')
    }
    
    pprint(result)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))
```

### 다른 전공자 예시

```python
import json
from pprint import pprint


def movie_info(movie):
    pass
    # 여기에 코드를 작성합니다.
    # pprint(movie)
    result = {
        'genre_ids': movie.get('genre_ids'),
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'poster_path': movie.get('poster_path'),
        'title': movie.get('title'),
        'vote_average':movie.get('vote_average')
    }
    
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))
```

> def는 함수 선언인데 리턴으로 주어야 한다. 강사님이 먼저 작성한 코드를 보면 파일을 이미 불러와서 변수에 할당해 주셨다. movie라는 변수를 활용만 하면 된다.

---

## 05. JSON 데이터 활용 - 영화 단일 정보 응용

- 영화 데이터 

  ``movie.json`` 와 ``genres.json`` 을  활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.

  - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
  - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.

- ``id``, ``title``,``vote_average``, ``overview``, ``genre_names``로 결과를 만듭니다. 

  (결과 예시 참고)

  - genre_names는 각 장르 정보를 값으로 가집니다.
  - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

### 결과 예시

```json
{'genre_names': ['Drama', 'Crime'],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```

### 내가 작성한 코드

```python
import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    f_movie = open('data/movie.json', 'r', encoding='utf-8')    
    f_genres = open('data/genres.json', 'r', encoding = 'utf-8')
    mv = json.load(f_movie)
    gr = json.load(f_genres)
    lst = []
    for i in mv.get('genre_ids'):
        for n in range(len(gr)):
            if gr[n]['id'] == i:
                lst.append(gr[n]['name'])
    result = {
        'genre_names' : lst,
        'id' : mv.get('id'),
        'title' : mv.get('title'),
        'vote_average' : mv.get('vote_average'),
        'overview' : mv.get('overview'),
    }

    pprint(result)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
```

### 다른 전공자 예시

```python
import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    movie_genre_ids = movie.get('genre_ids')
    movie_genre_names = [genre.get('name') for genre in genres if genre.get('id') in movie_genre_ids]
                
    result = {
        'genre_ids': movie_genre_names,
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average':movie.get('vote_average')
    }
    
    return result    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
```

> 코드는 오른쪽에서 왼쪽으로! 전공자의 코드는 역시 다르다...ㅋㅋㅋㅋ 한 줄로 끝내버리다니!!!
>
>  그래도 바로 저렇게 작성은 못해도 읽고 이해는 된다! 
>
> 조건 표현식이 가독성은 확실히 좀 떨어지는거 같기도 하다. 그래도 적응되면 정말 간단하게 작성 가능하겠다.



---

## 06. JSON 데이터 활용 - 영화 다중 정보 활용

- 영화 데이터 `movies.json` 와 `genres.json` 을  활용하여 필요한 정보로만 구성된 리스트를 출력하시오.

  - 코드는 선언된 함수 내에 작성하며, 결과 리스트를 반환합니다.
  - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.

- 전체 영화 정보는 평점 높은 20개의 영화 데이터입니다.  

  (결과 예시 참고)

  - 개별 영화 데이터는 `id`, `title`, `vote_average`, `overview`, `genre_names`로 구성된 딕셔너리입니다.
    - genre_names는 각 장르 정보를 값으로 가집니다.
    - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

**TIP. 이전 단계의 코드를 활용할 수 있습니다.**

### 결과 예시

```json
[{'genre_names': ['Drama', 'Crime'],
  'id': 278,
  'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '    
              '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '    
              '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '   
              '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
              '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
  'title': '쇼생크 탈출',
  'vote_average': 8.7},
 {'genre_names': ['Drama', 'Crime'],
  'id': 238,
  'overview': '시실리에서 이민온 뒤, 정치권까지 영향력을 미치는 거물로 자리잡은 돈 꼴레오네는 갖가지 고민을 호소하는 사람들의 '
              '문제를 해결해주며 대부라 불리운다. 한편 솔로소라는 인물은 꼴레오네가와 라이벌인 탓타리아 패밀리와 손잡고 새로운 '
              '마약 사업을 제안한다. 돈 꼴레오네가 마약 사업에 참여하지 않기로 하자, 돈 꼴레오네를 저격해 그는 중상을 입고 '
              '사경을 헤매게 된다. 그 뒤, 돈 꼴레오네의 아들 소니는 조직력을 총 동원해 다른 패밀리들과 피를 부르는 전쟁을 '
              '시작하는데... 가족의 사업과 상관없이 대학에 진학한 뒤 인텔리로 지내왔던 막내 아들 마이클은 아버지가 총격을 '
              '당한 뒤, 아버지를 구하기 위해 위험천만한 협상 자리에 나선다.',
  'title': '대부',
  'vote_average': 8.7},
 {'genre_names': ['Drama', 'History', 'War'],
  'id': 424,
  'overview': '2차 세계대전 당시 독일군이 점령한 폴란드. 시류에 맞춰 자신의 성공을 추구하는 기회주의자 쉰들러는 유태인이 '
              '경영하는 그릇 공장을 인수한다. 그는 공장을 인수하기 위해 나찌 당원이 되고 독일군에게 뇌물을 바치는 등 갖은 '
              '방법을 동원한다. 그러나 냉혹한 기회주의자였던 쉰들러는 유태인 회계사인 스턴과 친분을 맺으면서 냉혹한 유태인 '
              '학살에 대한 양심의 소리를 듣기 시작한다. 마침내 그는 강제 수용소로 끌려가 죽음을 맞게될 유태인들을 구해내기로 '
              '결심하고, 독일군 장교에게 빼내는 사람 숫자대로 뇌물을 주는 방법으로 유태인들을 구해내려는 계획을 세우는데...',
  'title': '쉰들러 리스트',
  'vote_average': 8.6},
...
```

### 내가 작성한 코드

```python
import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  

    f_movies = open('data/movies.json', 'r', encoding='utf-8')    
    f_genres = open('data/genres.json', 'r', encoding = 'utf-8')
    mvs = json.load(f_movies)
    gr = json.load(f_genres)
    lst = []
    mv_pop_score = []
    popular_idx = []
    hot_mv = []
    mvs_idx = []
    for i in range(len(mvs)):
        mv_pop_score.append(mvs[i]['popularity'])

    popular_idx = mv_pop_score
    popular_idx.sort(reverse=True)
    count = 0
    for score in popular_idx:
        count += 1
        mvs_idx.append(mv_pop_score.index(score))
        if count == 20:
            break
    for hot_idx in mvs_idx:
        mv = mvs[hot_idx]
        lst = []
        for i in mv.get('genre_ids'):
            for n in range(len(gr)):
                if gr[n]['id'] == i:
                    lst.append(gr[n]['name'])

        result = {
            'genre_names' : lst,
            'id' : mv.get('id'),
            'title' : mv.get('title'),
            'vote_average' : mv.get('vote_average'),
            'overview' : mv.get('overview'),
        }

        pprint(result)    
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```

### 다른 전공자 예시

```python
import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.
    movie_list = []
    
    for movie in movies:
        
        movie_genre_ids = movie.get('genre_ids')
        movie_genre_names = [genre.get('name') for genre in genres if genre.get('id') in movie_genre_ids]
                    
        result = {
            'genre_ids': movie_genre_names,
            'id': movie.get('id'),
            'overview': movie.get('overview'),
            'title': movie.get('title'),
            'vote_average':movie.get('vote_average')
        }
        
        movie_list.append(result)
        
    return movie_list 
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```

> 기가 맥히네. 어캐했노...ㅋㅋㅋㅋㅋㅋ
>
> 기존 5번에서 for문을 추가하였다. 기존 movie 변수 그대로 사용하도록 movies에서 가져오도록 구현하였다.
>
> 그리고 빈 리스트를 만들어서 기존에 하나만 만들어지던 딕셔너리를 모두 담아주도록 하여 구현한다.
