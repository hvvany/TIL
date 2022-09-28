from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Todo(models.Model):
  # django에서 pk(id)는 자동으로 만들어 준다.
  content = models.CharField(max_length = 80)
  # default = 값 안채우면 자동으로 채우기 값
  completed = models.BooleanField(default = False)
  