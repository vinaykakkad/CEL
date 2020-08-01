from django.urls import path

from .views import challenge_view, questions_view, answers_view, submission_view


urlpatterns = [
    path('challenges', challenge_view, name='challenge'),
    path('answer', answers_view, name='answer'),
    path('questions', questions_view, name='question'),
    path('submit', submission_view, name='submission')
]