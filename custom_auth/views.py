from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AuthSerializers,LoginSerializer,RegisterSerializer
from .models import AuthModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class SignupUser(APIView):
    # def get_object(self, id):
    #     try:
    #         return AuthModel.objects.get(pk=id)
    #     except AuthModel.DoesNotExist:
    #         raise NotFound(detail="User not found")
        
    # def delete(self, request, id):
    #     usr = self.get_object(id)  # Ensures 404 if user is not found
    #     usr.delete()
    #     return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)

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
        
class GetUserFromToken(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({"message": "User authenticated", "user": user.email})
        
# from rest_framework_simplejwt.tokens import AccessToken
# token_string = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQxNTk1MzE3LCJpYXQiOjE3NDE1OTE3MTcsImp0aSI6Ijc5MTI2NTg5YWFjZTQyMjE5MTI2NjA3MDY0ZmIwMzE2IiwidXNlcl9pZCI6NX0.QGfFI6_-6ka19KFwwrHQtiM5sdNwpslOaglL4Gn-pKE"
# token = AccessToken(token_string)

# print("User ID:", token["user_id"])
# print("Token Expiry:", token["exp"])
# exec("""from custom_auth.models import AuthModel; user_id = token["user_id"]; usr = AuthModel.objects.filter(id=user_id).first(); print("User exists:", usr.email) if usr else print("User not found")""")

# curl -X GET "http://127.0.0.1:8000/auth/detoken/" \
#      -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQxNTk1MzE3LCJpYXQiOjE3NDE1OTE3MTcsImp0aSI6Ijc5MTI2NTg5YWFjZTQyMjE5MTI2NjA3MDY0ZmIwMzE2IiwidXNlcl9pZCI6NX0.QGfFI6_-6ka19KFwwrHQtiM5sdNwpslOaglL4Gn-pKE"
# exec("""for email in duplicates:AuthModel.objects.filter(email=email).delete()""")