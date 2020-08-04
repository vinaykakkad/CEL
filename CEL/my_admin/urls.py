from django.urls import path

from .views import *


urlpatterns = [
    path('finishers', finishers_view, name='finishers'),
    path('answers', answers_view, name='answers'),
    path('addto50', add_to_50_view, name='add_to_50'),
    path('disqualified', add_to_disqualified, name='disqualified'),
    path('view50', display_50_view, name='view_50'),
    path('add_winner', add_to_winners, name='add_winner')
]