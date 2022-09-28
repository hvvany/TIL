from django.shortcuts import render
import random

import before_lifes

# Create your views here.
def fuck(request, number):
    if number % 2 == 0:
        answer = "짝수"
    else:
        answer = "홀수"
    context = {
        "answer": answer,
        "number": number,
    }

    return render(request, "even_odd.html", context)


def calculate(request, num1, num2):
    plus = num1 + num2
    minus = num1 - num2
    mult = num1 * num2
    dev = num1 // num2
    context = {
        "p": plus,
        "m": minus,
        "mu": mult,
        "d": dev,
        "num1": num1,
        "num2": num2,
    }
    return render(request, "add_minus.html", context)


def before(request):
    return render(request, "index.html")


def life(request):
    print(f' 와우 : {request.GET}')
    name = request.GET.get("name")
    lst = ["말", "소", "군인", "왕자"]
    choice = random.choice(lst)
    print(f'선택 : {choice}')
    context = {
        "before": choice,
        "name": name,
    }
    return render(request, "before_life.html", context)


def lorem(request):
  paragraph = request.GET.get('paragraph')
  word = request.GET.get('word')
  words = ['사과','귤','당근']
  result = []
  for _ in range(int(paragraph)):
    word_lst = []
    for _ in range(int(word)):
      w = random.choice(words)
      word_lst.append(w)
    result.append([word_lst])
  context = {
    'paragraph' : paragraph,
    'word' : word,
    'result' : result,
  }
  return render(request, 'lorem.html', context)
