from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class emp(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    status = models.BooleanField(null='TRUE')

class logindb(models.Model):
    username = models.CharField(max_length=50 , blank = 'FALSE')
    firstname = models.CharField(max_length=50, blank = 'FALSE')
    lastname = models.CharField(max_length=50, blank = 'TRUE')
    email = models.CharField(max_length=256,blank = 'FALSE')
    password = models.CharField(max_length=50,blank ='FALSE')
    role = models.CharField(max_length=1,blank = 'FALSE')
    def auth(uname , pwd):
        for all in logindb.objects.all():
            if uname == all.username and pwd == all.password:
                return True
        return None
    def checkname(uname):
        for all in logindb.objects.all():
            if uname == all.username:
                return True
        return None
    def getrole(uname , pwd):
        for all in logindb.objects.all():
            if uname == all.username and pwd == all.password:
                return all.role
    def getemail(uname):
        for all in logindb.objects.all():
            if uname == all.username:
                return all.email

class userinfo(models.Model):
    Dob = models.DateField(blank='FALSE')
    uname = models.CharField(max_length=50,blank='False',unique='true')
    cname = models.CharField(max_length=50,blank='False')
    Department = models.CharField(max_length=50,blank='False')
    sem = models.IntegerField(blank='False')
    yroj = models.IntegerField(blank='False')
    skilllist = ArrayField(ArrayField(models.CharField(max_length=10, blank=True),size=8),size=8)
    aoilist = ArrayField(models.CharField(max_length=10, blank=True),size=8)

class courses(models.Model):
    c_id = models.IntegerField((""),primary_key='true')
    C_title = models.CharField(max_length=50,blank='false')
    C_desp = models.CharField(max_length=50,blank='false')
    plat = models.CharField(max_length=200,blank='false')
    link = models.CharField(max_length=500,blank='false')
    skill = models.CharField(max_length=50,blank='false')
    rating = models.FloatField(blank='false')
    price = models.IntegerField(blank='false')

class usercu(models.Model):
    uname = models.CharField(max_length=50,blank='false')
    c_id = models.IntegerField(blank='False')
    sts = models.CharField(max_length=50,blank='false')
    token = models.CharField(max_length=50,blank='false',unique='true')
    def checks(tkn):
        for all in usercu.objects.all():
            if tkn == all.token:
                return True
        return None


class Cjob(models.Model):
    userid = models.CharField(max_length=120)
    j_id = models.AutoField(primary_key=True)
    company =models.CharField(max_length=120)
    title =  models.CharField(max_length=120)
    skills_req =  models.CharField(max_length=120)
    description =  models.CharField(max_length=120)  

class japp(models.Model):
    j_id = models.IntegerField(max_length=200)
    usename = models.CharField(max_length=100)    
    uemail = models.EmailField(max_length=254)
    sts = models.CharField(max_length=100)
    token = models.CharField(max_length=50,blank='false',unique='true')
    def checks(tkn):
        for all in japp.objects.all():  
            if tkn == all.token:
                return True
        return None


class help(models.Model):
    user = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    desc= models.TextField()
