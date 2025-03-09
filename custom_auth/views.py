from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AuthSerializers,LoginSerializer,RegisterSerializer
from .models import AuthModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class SignupUser(APIView):
    def post(self, request):
        #usr = AuthModel.objects.create(data=request.data )
        serializedUser = RegisterSerializer(data= request.data)
        if serializedUser.is_valid():
            usr= serializedUser.save()
            refresh =  RefreshToken.for_user(usr)
            access_token = str(refresh.access_token)
            return Response(
                {
                    "message": "User created successfully",
                    "access_token":access_token,
                    "data":serializedUser.data,
                    "refresh_token":str(refresh)
                }
            )
           
class SigninUser(APIView):
    def post(self, request):
        serializedUser = LoginSerializer(data=request.data)
        if serializedUser.is_valid():
            usr= AuthModel.objects.get(email= serializedUser.validated_data["email"])
            if not usr: 
                return Response({"message": "No user found with the given Mail id", "error": serializedUser.errors})

            if not usr.checkPassword(serializedUser.validated_data["password"]):
                return Response({"message": "Incorrect Password", "error": serializedUser.errors})
            
            refresh = RefreshToken.for_user(usr)
            access_token = str(refresh.access_token)
            return Response({
                "messages":"User signin successful",
                "access_token":access_token,
                "refresh":str(refresh)
            })