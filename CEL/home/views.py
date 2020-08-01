from django.shortcuts import render

# Create your views here.

def home_page_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home/home.html', context)

def leaderboard_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home/leaderboard.html', context)

def instruction_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home/instructions.html', context)
