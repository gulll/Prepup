from django.shortcuts import render

from django.http import Http404
# from models import User
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import GenericAPIView

# from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from django.contrib import auth
from django.contrib.auth import logout, login, authenticate

from prepup.serializers import UserSerializer
from prepup.serializers import UserProfileSerialize
from prepup.serializers import LoginSerializer
import json
from django.conf import settings


from .app_settings import (
    TokenSerializer, UserDetailsSerializer,
    PasswordResetSerializer, PasswordResetConfirmSerializer,
    PasswordChangeSerializer
)
# Create your views here.


class UserList(APIView):
    # permission_classes = [permissions.IsAuthenticated,]

    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # first save user
        # user = {
        #         "u_id" :    request.get['u_id'], 
        #         "name" :  request.get['name'],
        #         "email" :       request.get['email']
        #         }
        userSerializer = UserSerializer(data=request.DATA)
        if userSerializer.is_valid():
            try:
                userSerializer.save();
            except Exception, e:
                raise e
        else:
            return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationView(APIView):
    """ Allow registration of new users. """
    # permission_classes = ()
    # permission_classes = [permissions.IsAuthenticated,]

    # def post(self, request):
    #     serializer = RegistrationSerializer(data=request.data)

    #     # Check format and unique constraint
    #     if not serializer.is_valid():
    #         return Response(serializer.errors,\
    #                         status=status.HTTP_400_BAD_REQUEST)
    #     serializer.save()
    #     data = serializer.data

    #     print 'bhonddd****'

    #     # u = User(email=data['email'],password = data['password'])
    #     # print u
    #     # print dir(u)
    #     # u.save()

    #     # Create OAuth2 client
    #     # name = u.email
    #     # client = Client(user=u, name=name, url='' + name,\
    #     #         client_id=name, client_secret='', client_type=1)
    #     # client.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):


        request1 = json.loads(request.body)
        # user = {
        #         "username" :    request1.get('username', None), 
        #         "first_name" :  request1.get('first_name', None),
        #         "last_name" :   request1.get('last_name', None),
        #         "email" :       request1.get('email', None),
        #         "password" :    request1.get('password', None),
        #         }

        user = User.objects.create_user(username=request1.get('username', None),
                                email=request1.get('email', None),
                                password=request1.get('password', None))

        print(user)

        # first save user
        user1 = {
                "username" :    request.get['username'], 
                "first_name" :  request.get['first_name'],
                "last_name" :   request.get['last_name'],
                "email" :       request.get['email']
                }
        userSerializer = UserSerializer(data=user1)
        # if userSerializer.is_valid():
        #     try:
        #         userSerializer.save();
        #     except Exception, e:
        #         raise e
        # else:
        #     return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # user = User.objects.get(username=request1.get('username', None))
        # user.set_password(request1.get('password', None))
        user.save()

        # then save profile
        profile = {
                    "user" : userSerializer.data['id'],
                    "mobile" : request1.get('mobile',None),
                    "city" : request1.get('city',None),
                    "country" : request1.get('country',None),
                    "address" : request1.get('address',None),
                    "zip" : request1.get('zip',None),
                    "dob" : request1.get('dob',None),
                    "state" : request1.get('state',None),
                    "usercol" : request1.get('usercol',None),
                    "profile_image" : request1.get('profile_image',None),
                    "question_asked" : request1.get('question_asked',None),
                    "question_answered" : request1.get('question_answered',None),
                    "total_scored" : request1.get('total_scored',None),
                    }
        profileSerializer = UserProfileSerialize(data=profile)

        if (profileSerializer.is_valid()):
            try:
                
                profileSerializer.save();
                return Response(profileSerializer.data, status=status.HTTP_201_CREATED)
            except Exception, e:
                raise e
        else:
            return Response(profileSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # response = nativeLogin(request.POST, status)

        # if response.status_code == status.HTTP_400_BAD_REQUEST:
        #     return response;


# def nativeLogin(request,status):
#     if request.POST:
#         user = authenticate(username=request.POST['username'], password=request.POST['password'])
#         if user is not None:
#             if user.is_active:
#                 if not request.is_ajax():
#                     login(request, user)
#                     return HttpResponseRedirect("/")
#             else:
#                 return HttpResponse(_("Account not activated"), status=202)
#                 pass
#         else:
#             return HttpResponse(_("Wrong password or username"), status=405)
#             pass
#     #login succeddeed
#     return HttpResponse("Success",status=status.HTTP_200_OK)

class LogoutView(APIView):

    """
    Calls Django logout method and delete the Token object
    assigned to the current User object.
    Accepts/Returns nothing.
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass

        logout(request)

        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)

class MyProfile(APIView):
        
    def  get(self,request):
        current_user = request.user
        print(current_user)
        serializer = UserSerializer(current_user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(GenericAPIView):

    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.
    Calls Django Auth login method to register User ID
    in Django session framework
    Accept the following POST parameters: username, password
    Return the REST Framework Token Object's key.
    """
    permission_classes = (AllowAny,)
    token_model = Token
    serializer_class = LoginSerializer
    response_serializer = TokenSerializer

    def login(self,request):

        request1 = json.loads(request.body)
    
        username =   request1.get('username', None)
        password =   request1.get('password',None)
        # print(username)
        # print(password)
        # user1 = User.objects.get(username=username)
        # useer1.
        user = auth.authenticate(username = username,password=password)
        print(user)
        if user is not None:
            if user.is_active:
                if request.POST.get('remember_me', None):
                        request.session.set_expiry(604800)
                else:
                    request.session.set_expiry(604800)
                auth.login(request, user)
        # self.user = self.serializer.validated_data['user']
        self.token, created = self.token_model.objects.get_or_create(
            user=user)
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            login(self.request, user)

    def get_response(self):
        return Response(
            self.response_serializer(self.token).data, status=status.HTTP_200_OK
        )

    def get_error_response(self):
        return Response(
            self.serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def post(self, request, *args, **kwargs):
        request1 = json.loads(request.body)
    
        username =   request1.get('username', None)
        password =   request1.get('password',None)
        # print(username)
        # print(password)
        # self.serializer = LoginSerializer(data=request1)
        self.serializer = self.get_serializer(data=self.request.data)
        print(self.serializer)
        if not self.serializer.is_valid():
            return self.get_error_response()
        print(username)
        print(password)
        self.login(request)
        return self.get_response()
        