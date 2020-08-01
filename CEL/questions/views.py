import re
import json
from datetime import datetime

from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.db.models import Q

from account.models import Account
from .models import Question, Challenge, Answers

# Create your views here.


def only_letters(answer):
    match = re.match("^[a-z]*$", answer)
    return bool(match)


def challenge_view(request, *args, **kwargs):
    challenge = Challenge.objects.all()

    paginator = Paginator(challenge, 9)
    page = request.GET.get('page')
    page_data = paginator.get_page(page)

    context = {'page_data': page_data, 'last_page': paginator.num_pages}
    return render(request, 'questions/challenge.html', context)


def questions_view(request, *args, **kwargs):
    question_number = request.GET.get('question_number')
    challenge_number = request.GET.get('challenge_number')
    current_challenge = Challenge.objects.get(challenge_name=int(challenge_number))
    questions = current_challenge.questions.all().values()
    answers = Answers.objects.filter(answer_challenge=int(challenge_number), answer_user=request.user)
    answered_questions = list()

    for answer in answers:
        answered_questions.append(answer.answer_number)

    context = {'questions': list(questions),
               'answered_questions': json.dumps(answered_questions),
               'current_challenge': current_challenge,
               'challenge_number': challenge_number,
               'question_number': question_number}
    return render(request, 'questions/questions.html', context)


def answers_view(request, *args, **kwargs):
    answer_type = request.POST.get('type')
    username = request.POST.get('username')
    user = Account.objects.get(username=username)
    answer_no = int(request.POST.get('answer_no'))
    challenge_number = int(request.POST.get('challenge_number'))
    current_challenge = Challenge.objects.get(challenge_name=challenge_number)
    current_answer = None

    try:
        current_answer = request.user.answers.get(
            answer_number=answer_no, answer_challenge=current_challenge)
    except Exception as identifier:
        current_answer = None

    if answer_type == "textarea":
        answer = request.POST.get('answer')

        if current_answer == None:
            new_answer = Answers(answer_user=user, answer_number=answer_no,
                                 answer_type=answer_type, answer_textarea=answer,
                                 answer_challenge=current_challenge)
            new_answer.save()
        else:
            current_answer.answer_textarea = answer
            current_answer.save()
    else:
        answer = request.FILES['answer']

        if current_answer != None:
            current_answer.delete()
    
        new_answer = Answers(answer_user=user, answer_number=answer_no, 
                             answer_type=answer_type, answer_file=answer,
                             answer_challenge=current_challenge)
        new_answer.save()
    
    messages.info(request, 'Question ' + str(answer_no) + ' submitted successfully')

    
    if answer_no != current_challenge.get_total_ques():
        answer_no += 1
    else:
        answer_no = 1

    redirect_url = "/questions?challenge_number=" + \
        str(challenge_number) + "&question_number=" + \
        str(answer_no)

    return redirect(redirect_url)


def submission_view(request, *args, **kwargs):
    challenge_number = request.GET.get('challenge_number') 
    current_challenge = Challenge.objects.get(challenge_name=int(challenge_number))

    current_challenge.challenge_finishers.add(request.user)
    current_challenge.save()

    messages.info(request, 'Your quiz has been completed successfully. You can check your score now')
    return redirect('challenge')

    
    

# @login_required
# def congo_view(request, *args, **kwargs):

#     if request.user.get_current_que() != (MAX_QUESTIONS + 1):
#         messages.error(request, 'Complete all questions to get to that page!!')
#         return redirect('home')
#     return render(request, "congo.html", {})
