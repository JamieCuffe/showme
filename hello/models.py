from django.db import models

# Create your models here.
# class Greeting(models.Model):
#     when = models.DateTimeField('date created', auto_now_add=True)

#NEW

# class Certs(models.Model):

#    name = models.CharField(max_length = 50)
#    prereqs = models.CharField(max_length = 50)

#    class Meta:
#       db_table = "certs"

class Certificates(models.Model):

   title = models.CharField(max_length=100, primary_key=True)
   code = models.CharField(max_length=5)
   link_page = models.URLField()
   contact_name=models.CharField(max_length=255)
   contact_email=models.EmailField()
   total_courses=models.IntegerField()
   description=models.CharField(max_length=10000)
   tracks=models.CharField(default='', max_length=1000000)
   # track2=models.CharField(max_length=1000)
   # track3=models.CharField(max_length=1000)
   # track4=models.CharField(max_length=1000)
   # track5=models.CharField(max_length=1000)
   # track6=models.CharField(max_length=1000)
   class Meta:
   	db_table = "certificates"

class Students(models.Model):
    netid = models.CharField(max_length=100, primary_key=True)
    major = models.CharField(max_length=100, default='')
    degree = models.CharField(max_length=100, default='')
    year = models.IntegerField()
    certsObtained = models.CharField(max_length=1000000)
    numCoursesCompleted = models.IntegerField()
    certificateObtainable = models.IntegerField()
    coursesNeeded = models.IntegerField()
    courseBasket = models.CharField(max_length=1000000)
    coursesCompleted = models.CharField(max_length=1000000)
    pinnedCertificates = models.CharField(max_length=1000000)
    class Meta:
        db_table = "students"