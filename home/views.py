from django.shortcuts import render
from . models import *
from . forms import *
from django.http import JsonResponse

# Create your views here.def home(request):
def home(request):
    cat = Category.objects.all()
    pro = Product.objects.all()
    new = New.objects.all()
    post = Post.objects.all()
    

    return render(request, 'index.html' , {'p':pro , 'c':cat, 'n':new , 'b':post})

def sefaresh(request):
	if request.method == "POST":
		form = CustomOrderForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			return JsonResponse({'msg': 'Success'})
		else:
			return JsonResponse({'msg': 'ERRRR'})