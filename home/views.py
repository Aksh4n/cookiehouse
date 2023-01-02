from django.shortcuts import render
from . models import *

# Create your views here.def home(request):
def home(request):
    cat = Category.objects.all()
    pro = Product.objects.all()
    new = New.objects.all()
    post = Post.objects.all()
    

    return render(request, 'index.html' , {'p':pro , 'c':cat, 'n':new , 'b':post})

