from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"main/index.html")
#    return HttpResponse("Welcome to main index.<br><a href = student_app/>Здесь ссылка</a>")
