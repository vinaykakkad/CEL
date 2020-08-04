from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages

from questions.models import Challenge
from account.models import Account
from CEL.settings import MAXIMUM_SELECTED, MAXIMUM_WINNERS
# Create your views here.


def finishers_view(request, *args, **kwargs):
    challenge_number = request.GET.get('challenge_number')
    challenge = Challenge.objects.get(challenge_name=int(challenge_number))
    finishers = challenge.challenge_finishers.all()
    disqualified = challenge.disqualified.all()
    selected = challenge.selected.all()

    paginator = Paginator(finishers, 20)
    page = request.GET.get('page')
    page_data = paginator.get_page(page)

    context = {'page_data': page_data, 'last_page': paginator.num_pages,
               'challenge_number': int(challenge_number), 'selected': selected,
               'disqualified': disqualified
        }
    return render(request, 'admin/finishers.html', context)

def answers_view(request, *args, **kwargs):
    challenge_number = request.GET.get('challenge_number')
    username = request.GET.get('username')
    current_user = Account.objects.get(username=username)
    answers = current_user.answers.filter(answer_challenge=int(challenge_number))

    context = {'answers': answers, 'username': username,
               'challenge_number': challenge_number
        }
    return render(request, 'admin/answers.html', context)

def add_to_50_view(request, *args, **kwargs):
    challenge_number = request.GET.get('challenge_number')
    username = request.GET.get('username')
    current_user = Account.objects.get(username=username)
    current_challenge = Challenge.objects.get(challenge_name=int(challenge_number))

    if current_challenge.selected.count() >= MAXIMUM_SELECTED:
        messages.error(request, str(MAXIMUM_SELECTED) + ' Students have been already selected!!')
        return redirect('/finishers?challenge_number='+str(challenge_number))
    else:
        current_challenge.selected.add(current_user)
        current_challenge.save()

    message = username + " has been successfully added to the 50" 
    messages.info(request, message)
    return redirect('/finishers?challenge_number='+str(challenge_number))

def add_to_disqualified(request, *args, **kwargs):
    challenge_number = request.GET.get('challenge_number')
    username = request.GET.get('username')
    current_user = Account.objects.get(username=username)
    current_challenge = Challenge.objects.get(challenge_name=int(challenge_number))

    current_challenge.disqualified.add(current_user)
    current_challenge.save()

    message = username + " has been successfully removed" 
    messages.info(request, message)
    return redirect('/finishers?challenge_number='+str(challenge_number))
    
def display_50_view(request, *args, **kwargs):
    challenge_number = request.GET.get('challenge_number')
    current_challenge = Challenge.objects.get(challenge_name=int(challenge_number))
    selected = current_challenge.selected.all()

    context = {'selected': selected, 'challenge_number': challenge_number}
    return render(request, 'admin/view50.html', context)

def add_to_winners(request, *args, **kwargs):
    challenge_number = request.GET.get('challenge_number')
    username = request.GET.get('username')
    current_user = Account.objects.get(username=username)
    current_challenge = Challenge.objects.get(challenge_name=int(challenge_number))

    if current_challenge.challenge_winners.count() >= MAXIMUM_WINNERS:
        messages.error(request, str(MAXIMUM_WINNERS) + ' winners have been already selected!!')
        return redirect('/view50?challenge_number='+str(challenge_number))
    else:
        current_challenge.challenge_winners.add(current_user)
        current_challenge.save()

    message = username + " has been successfully added as a winner" 
    messages.info(request, message)
    return redirect('/view50?challenge_number='+str(challenge_number))


