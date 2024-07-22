from django.shortcuts import render
from .models import News,Category
# Create your views here.
def index(request):
    category = Category.objects.all()
    news = News.objects.all()
    return render(request,'index.html',{'data':news,'category':category})

def detail(request,id):
    data = News.objects.get(id = id)
    return render(request,'single.html',{'data':data})

