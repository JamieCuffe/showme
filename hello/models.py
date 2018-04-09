from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

#NEW

class Certs(models.Model):

   name = models.CharField(max_length = 50)
   prereqs = models.CharField(max_length = 50)

   class Meta:
      db_table = "certs"

#NEW
# class Certificates(models.Model):
# 	title = models.CharField(max_length=100)
# 	code = models.CharField(max_length=5)
# 	link_page=models.URLField()
# 	contact_name=models.CharField(max_length=255)
# 	contact_email=models.EmailField()
# 	total_courses=models.IntegerField()
# 	description=models.CharField(max_length=10000)
# 	track1=models.CharField(max_length=1000)
# 	track2=models.CharField(max_length=1000)
# 	track3=models.CharField(max_length=1000)
# 	track4=models.CharField(max_length=1000)
# 	track5=models.CharField(max_length=1000)
# 	track6=models.CharField(max_length=1000)

# 	class Meta:
#       db_table = "certificates"

#END NEW




