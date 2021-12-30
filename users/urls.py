from django.urls import path, include
from .views import *

urlpatterns = [
   path('',user_signin,name='authen'), # default path in our app
]
