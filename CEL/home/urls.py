from django.urls import path

from .views import home_page_view, instruction_view, leaderboard_view


urlpatterns = [
    path('', home_page_view, name='home'),
    path('instructions', instruction_view, name='instructions'),
    path('leaderboard', leaderboard_view, name='leaderboard'),
]
