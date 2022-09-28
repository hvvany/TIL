from django.shortcuts import render
import random

# Create your views here.
def index(request):
  # 메인 페이지를 보여 준다.
  names = ['홍길동','고길동','장길동']

  name = random.choice(names)

  context = {
    'name' : name,
    'img' : 'https://www.youtube.com/redirect?event=live_chat&redir_token=QUFFLUhqbEF2YTR4aHM1WnV2dmxwdDdLM2hEekQ1eGJrUXxBQ3Jtc0tsbHVVUi1XenBYdkJvUlZ6TVdENi1kd25BeG5GdlFDWWhYNlFtYkNIOHlyNmZ2NHhVemM0ODA2aDRYX3hBQ3F0Q1RoZUozenpXeE9kck5wczBRVmxUcUNpVGpMb1dSRkJEYWNLbjNuWjhtZDcteTk3QQ&q=https%3A%2F%2Fcdn.crowdpic.net%2Fdetail-thumb%2Fthumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
  }
  return render(request,'index.html', context)

def welcome(request,name):
  # 사람들이 /welcome/본인이름 을 입력하면, 환영 인사화 이름을 동시에 보여준다.
  context = {
    'name' : name,
  
  }
  return render(request, 'welcome.html', context)