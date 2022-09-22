# Django 템플릿 언어

#django #templates #language



## 변수

 

```
{{ 변수 }}
```

변수는 {{ 변수 }} 로 사용 됩니다. 

템플릿 엔진이 변수를 만나면, 평가하여 그 결과를 치환합니다. 

변수명은 밑줄("_")과 영문으로 이뤄지며 공백이나 특수문자는 사용할 수 없습니다.

변수명에서 점(".")은 기술적으로 변수의 속성에 접근할 때 사용됩니다.

 

```
{{ section.title }
```

이 경우 section 개체의 title 속성으로 치환됩니다.

 

------

## 필터

 

필터를 사용함으로써 변수의 표시에 변화를 줄 수 있습니다.

 

```
{{ 변수명 | 내장 필터 }}
```

변수의 길이를 반환하거나, 변수의 앞의 n개의 단어만 반환하거나, 변수를 모두 소문자로 변경하거나 등의

여러가지 기능을 제공합니다.

 

```
{{ name|lower }}   # {{ name }}변수에 lower 필터를 적용하여 텍스트를 소문자로 변경시킨 결과를 출력.

{{ name|length }}  # {{ name }}변수에 값의 길이를 반환합니다.

{{ name|striptags }}  # {{ name }}변수에 포함된 HTML 태그를 제거합니다.
```

 

------

## 태그

 

Django에서는 스무개가 넘는 템플릿 태그가 내장되어 있습니다.

템플릿 태그의 종류에는 반복문, 조건문, 상속 등이 있습니다.

 

```
{% 태그 %}
```

태그는 {% 태그 %} 형태로 사용합니다.

 

## if 태그

 

```
{% if latest_question_list %}
    <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
{% else %}
    <p>No latest_question_list are available.</p>
{% endif %}
```

 

latest_question_list 이 존재할 경우

\<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a>\</li> 를 출력하고

존재하지 않을 경우 \<p>No polls are available.\</p>를 출력합니다.

또한 if 태그에 각종 연산자도 사용할 수 있습니다.

 

```
{% if latest_question_list|length > 5 %}
    <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
{% else %}
    <p>No latest_question_list are available.</p>
{% endif %}
```

 

 

 

## 반복문

 

```
{% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
{% endfor %}
```

for 태그는 endfor로 끝을 알립니다.
