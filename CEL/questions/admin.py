from django.contrib import admin

from .models import Question, Challenge, Answers


admin.site.register(Question)
admin.site.register(Challenge)
admin.site.register(Answers)
