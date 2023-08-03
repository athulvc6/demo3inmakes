from django.shortcuts import render
from .models import place,position
# Create your views here.
def demo(request):
    obj1=place.objects.all()
    obj=position.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
