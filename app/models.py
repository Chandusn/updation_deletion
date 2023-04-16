from django.db import models

# Create your models here.
class Course(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)
    tname=models.CharField(max_length=100)

    def __str__(self):
        return self.cid

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    marks=models.IntegerField()
    cid=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.sid
    


    