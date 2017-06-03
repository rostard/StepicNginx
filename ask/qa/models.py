from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
	def new(self):
		pass
	def popular(self):
		pass

class Question(models.Model):
	objects=QuestionManager()
	title = models.CharField (max_length=255)
	text = models.TextField()
	added_at = models.DateField()
	rating = models.IntegerField()
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User)

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField()
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


