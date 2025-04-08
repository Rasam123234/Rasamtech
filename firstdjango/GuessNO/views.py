from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def discount(request):
    return render(request,"Discount.html")