from django.db import models

# Create your models here.
class User(models.Model):
    u_account = models.CharField(max_length=32,unique=True)
    u_id = models.CharField(max_length=256,unique=True)
    u_password = models.CharField(max_length=30,default='sf1234')
    u_authority = models.CharField(max_length=256)
    u_department = models.CharField(max_length=30)
    u_name = models.CharField(max_length=32)
    is_delete = models.BooleanField(default=False)
    u_telephone = models.CharField(max_length=32)

    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
         return '%d: %s' % (self.pk, self.u_account)



class Student(models.Model):
    name = models.CharField(u'姓名', max_length=100, default='no_name')
    sex = models.CharField(u'性别',max_length=50,default='male')
    sid = models.CharField(u'学号',max_length=100,default='0')
 
    def __unicode__(self):
        return '%d: %s' % (self.pk, self.name)

