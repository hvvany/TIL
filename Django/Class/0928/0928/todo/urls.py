from django.urls import path
from . import views

# url namespace
# url을 이름으로 분류하는 기능

app_name = 'todo'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('delete/<int:todo_pk>', views.delete, name='delete'),
  path('completed/<int:todo_pk>', views.completed, name='completed'),
  path('edit/<int:todo_pk>', views.edit, name='edit'),
]