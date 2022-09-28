from django.shortcuts import render
import random

# Create your views here.
def index(request):

  menus = ['삼겹살','떡볶이','돈까스',]
  menu = random.choice(menus)

  context = {
    'name' : menu,
    'img_sam' : 'https://image.utoimage.com/preview/cp871385/2018/11/201811010095_500.jpg',
    'img_ddo' : 'https://media.istockphoto.com/photos/tteokbokki-with-eggs-in-gray-bowl-on-concrete-table-top-tteokbokki-is-picture-id1253629795?k=20&m=1253629795&s=612x612&w=0&h=T8lIYZE8v38tCSHIsURjUizjswXZ8tqXc6qgNtNjhJ0=',
    'img_don' : 'https://media.istockphoto.com/photos/tonkatsu-picture-id1156023976?k=20&m=1156023976&s=612x612&w=0&h=6wcljfmMHy1Tg53PxNPU3UGdatX70AblpR9GExYSMqo=',
  }

  return render(request,'index.html',context)
