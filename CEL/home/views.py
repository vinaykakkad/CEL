from django.shortcuts import render

from account.models import Account

# Create your views here.

def home_page_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home/home.html', context)

def leaderboard_view(request, *args, **kwargs):
    accounts = Account.objects.all()
    winners = list()

    for account in accounts:
        if account.challenges_won.count() > 0:
            winners.append(account)

    context = {'winners': winners}
    return render(request, 'home/leaderboard.html', context)

def instruction_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home/instructions.html', context)
