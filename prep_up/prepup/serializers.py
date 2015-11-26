# from django.contrib.auth.models import User
from models import Profile
from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # name                      = serializers.CharField(max_length=45)
    # email                     = serializers.CharField(max_length=45)
    # password                  = serializers.CharField(max_length=45)
    # mobile                    = serializers.CharField(max_length=45)
    # city                      = serializers.CharField(max_length=45)
    # country                   = serializers.CharField(max_length=45)
    # address                   = serializers.CharField(max_length=45)
    # zip                       = serializers.CharField(max_length=45)
    # dob                       = serializers.CharField(max_length=45)
    # state                     = serializers.CharField(max_length=45)
    # usercol                   = serializers.CharField(max_length=45)
    # profile_image             = serializers.CharField(max_length=200)
    # question_asked            = serializers.IntegerField()
    # question_answered         = serializers.IntegerField()
    # total_scored              = serializers.IntegerField()
    # user_id              = serializers.IntegerField(default = 0 , primary_key = True)


    # user                      = serializers.OneToOneField(User, related_name="profile")
    # mobile                    = serializers.CharField(max_length=45)
    # city                      = serializers.CharField(max_length=45)
    # country                   = serializers.CharField(max_length=45)
    # address                   = serializers.CharField(max_length=45)
    # zip                       = serializers.CharField(max_length=45)
    # dob                       = serializers.CharField(max_length=45)
    # state                     = serializers.CharField(max_length=45)
    # usercol                   = serializers.CharField(max_length=45)
    # profile_image             = serializers.CharField(max_length=200)
    # question_asked            = serializers.IntegerField()
    # question_answered         = serializers.IntegerField()
    # total_scored              = serializers.IntegerField()

    class Meta:
        model = User
        field = ('email')

# class ProfileSerialize(serializers.ModelSerializer):

#     mobile                    = serializers.CharField(max_length=45)
#     city                      = serializers.CharField(max_length=45)
#     country                   = serializers.CharField(max_length=45)
#     address                   = serializers.CharField(max_length=45)
#     zip                       = serializers.CharField(max_length=45)
#     dob                       = serializers.CharField(max_length=45)
#     state                     = serializers.CharField(max_length=45)
#     usercol                   = serializers.CharField(max_length=45)
#     profile_image             = serializers.CharField(max_length=200)
#     question_asked            = serializers.IntegerField()
#     question_answered         = serializers.IntegerField()
#     total_scored              = serializers.IntegerField()
#     class Meta:
#         model = User
        # fields = ('email', 'password')


class UserProfileSerialize(serializers.ModelSerializer):

    city                      = serializers.CharField(required=False, max_length=45, allow_blank=True,allow_null=True)
    mobile                    = serializers.CharField(required=False, max_length=45, allow_blank=True,allow_null=True)
    country                   = serializers.CharField(required=False, max_length=45, allow_blank=True,allow_null=True)
    address                   = serializers.CharField(required=False, max_length=45, allow_blank=True,allow_null=True)
    zip                       = serializers.CharField(required=False, max_length=45, allow_blank=True,allow_null=True)
    dob                       = serializers.CharField(required=False, max_length=45, allow_blank=True,allow_null=True)
    state                     = serializers.CharField(required=False, max_length=45, allow_blank=True,allow_null=True)
    usercol                   = serializers.CharField(required=False, max_length=45, allow_blank=True,allow_null=True)
    profile_image             = serializers.CharField(required=False, max_length=100, allow_blank=True,allow_null=True)
    question_asked            = serializers.IntegerField(required=False,allow_null=True)
    question_answered         = serializers.IntegerField(required=False,allow_null=True)
    total_scored              = serializers.IntegerField(required=False,allow_null=True)
    class Meta:
        model = Profile
        # fields = ('phone_number', 'avatar', 'banner', 'user')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
        