# memory_new



- ## packing, unpacking

  > packing : 패킹은 인자로 받은 `여러개의 값을 하나의 객체`로 합쳐서 받을 수 있도록 합니다.
  >
  > 위치인자 패킹은 `*`한 개 를 매개변수 앞에 붙임으로 사용합니다.

  ```python
  def func(*args):    #  매개변수 앞에 *
        print(args)
        print(type(args))
      
  func(1, 2, 3, 4, 5, 6, 'a', 'b')
  
  # 결과
  (1, 2, 3, 4, 5, 6, 'a', 'b')
  <class 'tuple'>
  ```

  > unpacking : `packing`은 여러개의 객체를 하나의 객체로 합쳐주었습니다. `unpacking`은 여러개의 객체를 포함하고 있는 하나의 객체를 풀어줍니다.
  >
  > 함수에서 `unpacking`을 할때는, 매개변수에서 `*`을 붙이는게 아니라 인자 앞에 `*`을 붙여서 사용합니다.

  ```python
  a = [1,2,3,4]
  print(a)
  print(*a)
  
  # 결과
  [1, 2, 3, 4]
  1 2 3 4
  ```



- ## set 합집합, 교집합, 차집합

  - 합집합 ( | )

    ```python
    >>> s1 = {1, 2, 3, 4, 5}
    >>> s2 = {4, 5, 6, 7}
    >>> s1|s2
    {1, 2, 3, 4, 5, 6, 7}
    ```

  - 교집합 ( & )

    ```python
    >>> s1 = {1, 2, 3, 4, 5}
    >>> s2 = {4, 5, 6, 7}
    >>> s1 & s2
    {4, 5}
    ```

  - 차집합 ( - )

    ```python
    >>> s1 = {1, 2, 3, 4, 5}
    >>> s2 = {4, 5, 6, 7}
    >>> s1 - s2
    {1, 2, 3}
    ```

  - 대칭차집합 ( ^ )

    ```python
    set1 = {'A', 'B', 'C', 'D'}
    set2 = {'C', 'D', 'E', 'F'}
    sym_diff = set1 ^ set2
    print( sym_diff )
    {'F', 'B', 'E', 'A'}
    ```

    

- ## permutations

  > **itertools. permutations(iterable, r=None)**

  > 순열 nPr  할 때 p가 permutation 이다.

  ```python
  import itertools
  
  arr = ['A', 'B', 'C']
  nPr = itertools.permutations(arr, 2)
  print(list(nPr))
  
  결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
  ```

  

### 

- ## combination

  > **itertools. combinations(*iterable*, *r*)**
  >
  > 조합 nCr 할 때 C가 combination 이다.

  ```python
  import itertools
  
  arr = ['A', 'B', 'C']
  nCr = itertools.combinations(arr, 2)
  print(list(nCr))
  
  결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]
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