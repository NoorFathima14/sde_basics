from rest_framework.urls import path
from .views import SignupUser,SigninUser, GetUserFromToken

urlpatterns = [
    # URLs
    path("signup/", SignupUser.as_view(), name="signup-user"),  
    path("signin/", SigninUser.as_view(), name="signin-user"),  
    path("detoken/", GetUserFromToken.as_view(), name="detokenize-user"),  
]