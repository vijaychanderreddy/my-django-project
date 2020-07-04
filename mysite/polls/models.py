from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date posted')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


review_code = (("50","1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))


class Review(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    review_choice = models.CharField(max_length=20,
                                     choices=review_code,
                                     default='0'
                                     )

    def __str__(self):
        return self.review_choice
