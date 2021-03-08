from django.shortcuts import render, redirect


def show_city(request):
    return render(request,'index.html')