from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = patterns('',
    # url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^list/', views.UserList.as_view()),
    url(r'^register/',views.RegistrationView.as_view()),
    url(r'^login/',views.LoginView.as_view()),
    url(r'^logout/',views.LogoutView.as_view()),
    url(r'^me/',views.MyProfile.as_view()),
)
