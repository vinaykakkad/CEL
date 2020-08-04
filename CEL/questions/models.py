import pytz
from datetime import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from account.models import Account

# Create your models here.
class Challenge(models.Model):
    challenge_name = models.IntegerField()
    challenge_winners = models.ManyToManyField(Account, related_name='challenges_won', blank=True)
    challenge_finishers = models.ManyToManyField(Account, related_name='challenges_finished', blank=True)
    selected = models.ManyToManyField(Account, related_name='challenges_selected', blank=True)
    disqualified = models.ManyToManyField(Account, related_name='challenges_disqualified', blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return str(self.challenge_name)

    def get_total_ques(self):
        return self.questions.count()

    def get_current_datetime(self):
        return datetime.now(tz=self.start_date.tzinfo)

    def is_challenge_active(self):
        if self.get_current_datetime() > self.start_date and self.get_current_datetime() < self.end_date:
            return True
        else:
            return False


answer_types = (
    ("1", "textarea"),
    ("2", "file")
)

class Question(models.Model):
    question_challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='questions')
    question_number = models.IntegerField()
    question_text = models.TextField(null=True,blank=True)
    question_image = models.ImageField(upload_to='gallery',null=True,blank=True)
    answer_type = models.CharField(max_length=10, choices=answer_types)

    def __str__(self):
        return str(self.question_challenge) + "." + str(self.question_number)


class Answers(models.Model):
    answer_user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='answers')
    answer_challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='answers')
    answer_number = models.IntegerField()
    answer_type = models.CharField(max_length=10, choices=answer_types)
    answer_textarea = models.TextField(null=True, blank=True)
    answer_file = models.FileField(upload_to='answers', null=True, blank=True)

    def __str__(self):
        return self.answer_user.username + "." + str(self.answer_challenge.challenge_name) + "." + str(self.answer_number)

    def delete(self, *args, **kwargs):
        self.answer_file.delete()
        super().delete(*args, **kwargs)


# class FinishedTime(models.Model):
#     finished_time = models.DateTimeField()
#     user = models.ForeignKey(Account)
#     challenge = models.ForeignKey(Challenge)
