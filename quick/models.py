# -*- coding: utf-8 -*-
from django.db import models, transaction
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.utils.functional import cached_property
from django_rq import enqueue
import datetime


class Profile(models.Model):
	user = models.OneToOneField(User,primary_key = True)
	
	#school = models.ForeignKey('control.School', null = True)
	
class Teacher(models.Model):
	profile = models.ForeignKey(Profile)
	school = models.ForeignKey(School)
	
	class Meta:
		db_table = 'teacher'
	
class Student(models.Model):
	profile = models.ForeignKey(Profile)
	teacher = models.ForeignKey(Teacher)
	class_number = models.IntegerField(default=1)
	
	class Meta:
		db_table = 'student'

class School(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return "%s" % (self.name)

class Feeling(models.Model):
	domain_choices = {
		('1', 'Home'),
		('2', 'Self'),
		('3', 'Love'),
		('4', 'School'),
		('5', 'Friends')
	}
	
	base_choices = {
		('1', 'Good'),
		('2', 'Bad'),
	}
	
	secondary_choices = {
		('1', 'Sad'),
		('2', 'Happy'),
		('3', 'Angry'),
		('4', 'Afraid'),
		('5', 'Surprise')
	}
	
	tertiary_choices = {
		#Happy
		('1', 'Content'),
		('2', 'Proud'),
		('3', 'Optimistic'),
		('4', 'Relieved'),
		('5', 'Joy'),
		('23', 'Excited')
		#Surprised
			#Good
		('6', 'Amazed'),
		('7', 'Shocked'),
			#Bad
		('8', 'Startled'),
		#Anger
		('9','Annoyed'),
		('10','Jealous'),
		('11','Hate'),
		('12', 'Frustrated'),
		('13', 'Revenge'),
		#Sadnes
		('14','Sad'),
		('15', 'Ashamed'),
		('16','Guilty'),
		('17', 'Rejected')
		('18', 'Lonely')
		#Fear
		('19','Anxious'),
		('20', 'Stressed'),
		('21', 'Panicked'),
		('22', 'Terrified'),
	}
	
	student = models.ForeignKey(Student)
	domain = models.CharField(max_length = 50, choices = domain_choices)
	base_feeling = models.CharField(max_length = 50, choices = base_choices)
	secondary_feeling = models.CharField(max_length = 50, choices = secondary_choices)
	tertiary_feeling = models.CharField(max_length = 50, choices = tertiary_choices)
	created_ts = models.DateTimeField(auto_now_add=True)
	
	
	
	
	
		
