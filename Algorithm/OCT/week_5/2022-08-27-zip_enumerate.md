# 베스트 앨범 사기버전



```python
def solution(genres, plays):
  answer = []

  dic1 = {}
  dic2 = {}

  for i, (g, p) in enumerate(zip(genres, plays)):  # (0, (genre, plays)),(1, (genre, plays)),...
    if g not in dic1:
      dic1[g] = [(i, p)]
    else:
      dic1[g].append((i, p))      # dic1 : {'classic' : [(0,500),(2,150),(3,800)],'pop' : [(1,600),(4,2500)]}

    if g not in dic2:
      dic2[g] = p
    else:
      dic2[g] += p                # dic2 : {'classic' : 1450, 'pop' : 3100 }

  for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):   # dic2 값 기준으로 내림차순 정렬하여 하나씩 불러옴
    for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:  # dic1의 값 튜플의 1번 인덱스 재생수 내림차순 2개 정렬로 불러옴
      answer.append(i)            # answer = [4, 1, 3, 0]

  return answer
```



## [enumerate 함수](https://docs.python.org/ko/3/library/functions.html#enumerate)

> ### `enumerate`(*iterable*, *start=0*)

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']

list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```



## [zip 함수](https://docs.python.org/ko/3.7/library/functions.html#zip)

> ### `zip`(iterables)

```python
x = [1, 2, 3]
y = [4, 5, 6]

zipped = zip(x, y)

list(zipped)
[(1, 4), (2, 5), (3, 6)]
```



## [sorted 키 함수](https://docs.python.org/ko/3/howto/sorting.html)

> ### `sorted`(정렬할 데이터)
>
> ### `sorted`(정렬할 데이터, reverse = False)
>
> ### `sorted`(정렬할 데이터, key = <함수> , reverse = False)

> #### [`list.sort()`](https://docs.python.org/ko/3/library/stdtypes.html#list.sort)와 [`sorted()`](https://docs.python.org/ko/3/library/functions.html#sorted)는 모두 비교하기 전에 각 리스트 요소에 대해 호출할 `함수`(또는 다른 콜러블)를 지정하는 *key* 매개 변수를 가지고 있습니다.

```python
sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
```

```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted(student_tuples, key=lambda x: x[2])       # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```



## [lambda 함수](https://wikidocs.net/22804)

> ### lambda [parameters] : expression

```python
def <lambda>(parameters):
    return expression
```



![이미지](https://wikidocs.net/images/page/22804/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2018-11-07_05.56.24.png)