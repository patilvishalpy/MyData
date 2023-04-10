from django.db import models

class coursedata(models.Model):
    course_no=models.IntegerField()
    course_name=models.CharField(max_length=40)
    timing=models.TimeField()
    starting_date=models.DateField()
    duration=models.CharField(max_length=40)
    fees=models.IntegerField()
    trainer_name=models.CharField(max_length=40)

class feedbackdata(models.Model):
    name=models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    subject=models.CharField(max_length=100)
    messange=models.CharField(max_length=200)

class reviews(models.Model):
    name=models.CharField(max_length=30)
    ratings=models.CharField(max_length=30)
    comments=models.CharField(max_length=100)
