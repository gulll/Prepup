from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    # user			          = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # name                      = models.CharField(max_length=45)
    # email                     = models.CharField(max_length=45)
    # password                  = models.CharField(max_length=45)
    user                      = models.OneToOneField(User, related_name="profile")
    
    address                   = models.CharField(max_length=45)
    mobile                    = models.CharField(max_length=45)
    city                      = models.CharField(max_length=45)
    country                   = models.CharField(max_length=45)
    zip                       = models.CharField(max_length=45)
    dob                       = models.CharField(max_length=45)
    state                     = models.CharField(max_length=45)
    usercol                   = models.CharField(max_length=45)
    profile_image             = models.CharField(max_length=200)
    question_asked            = models.IntegerField()
    question_answered         = models.IntegerField()
    total_scored              = models.IntegerField()
    # user_id              = models.IntegerField(default = 0 , primary_key = True)

    def __unicode__(self):
        return unicode(self.user)

    # def __init__(self,email,password):
    # 	# super(User, self).__init__(email,password)
    # 	# self.email = email
    # 	# self.name  = name
    # 	# self.mobile = mobile
    # 	self.password = password
    # 	# self.dob = dob


	# def __str__(self):
	# 	return "%s's detail" % self.user 
   
