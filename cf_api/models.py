from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
 
    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(u'姓名', max_length=100, default='no_name')
    sex = models.CharField(u'性别',max_length=50,default='male')
    sid = models.CharField(u'学号',max_length=100,default='0')
 
    def __unicode__(self):
        return '%d: %s' % (self.pk, self.name)
