from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	objects=QuestionManager()
	title = models.CharField (max_length=255)
	text = models.TextField()
	added_at = models.DateField()
	rating = models.IntegerField()
	author = ForeignKey(User)
	likes = ManyToManyField(User)

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField()
	question = ForeignKey(Question)
	author = ForeignKey(User)

class QuestionManager(models.Manager):
	def new(self):
		pass
	def popular(self):
		pass
