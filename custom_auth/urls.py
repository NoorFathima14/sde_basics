from rest_framework.urls import path
from .views import SignupUser,SigninUser

urlpatterns = [
    # URLs
    path("signup/", SignupUser.as_view(), name="signup-user"),  
     path("signin/", SigninUser.as_view(), name="signin-user"),  
]