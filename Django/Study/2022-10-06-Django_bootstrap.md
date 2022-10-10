## 장고에서 부트스트랩 사용하기
### 1. bootstrap pip 설치
```bash
$ pip install django_bootstrap5
```
### 2. INSTALLED_APPS에 추가
```python
INSTALLED_APPS = [
    'articles',
    'bootstrap5'
    ...
]
```
### 3. load bootstrap5
> load는 python의 import와 같다. 따라서 base.html에 사용해도 사용할 때마다 불러줘야 한다.
> 사용 예는 다음과 같다.

#### 1. base.html에 css/ javascript불러오기
```html
{% load django_bootstrap5 %}
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  {% bootstrap_css %}
  {% block css %}{% endblock css %}
</head>
<body>
  <div class="container">
    {% block body %}{% endblock body %}
  </div>
  {% bootstrap_javascript %}
</body>

</html>
```

#### 2. 모델 폼에 부트스트랩 적용하기

```html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %} 
<h1>글 수정하기</h1>

<form action="" method="POST">
  {% csrf_token %}
  {% bootstrap_form article_form %}
  {% bootstrap_button button_type="submit" content="OK" %}
</form>
{% endblock %}
```