from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def ping(request):
    return render(request, "ping.html")


def pong(request):
    # print(request)
    # print(dir(request))
    name = request.GET.get("ball")
    context = {"name": name}
    return render(request, "pong.html", context)
