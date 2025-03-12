from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel, BookModel
from .serializers import UserSerializer, BookSerializer
from django.shortcuts import get_object_or_404

class UserView(APIView):
    def get(self, request):
        usrs = UserModel.objects.all() #returns all details
        serialized_users = UserSerializer(usrs, many=True) #many true-> when ur trying to serialize many details
        return Response(serialized_users.data)
    
    def post(self, request): #request-> what user is sending to us and who is sending?
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid(): #checks if the data being send is correct as in not img in txt field
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class UserViewWithIds(APIView):
    def get_object(self,id):
        try:
            usr = UserModel.objects.get(pk=id)
            return usr
        except: 
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request,id):
        usr = self.get_object(id)
        serializer = UserSerializer(usr)
        return Response(serializer.data)
    
    def put(self, request, id):
        usr = self.get_object(id)
        serializerUser= UserSerializer(usr, data = request.data)

        if serializerUser.is_valid():
            serializerUser.save()
            return Response(serializerUser.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,id):
        usr = self.get_object(id)
        usr.delete()
        return Response(status= status.HTTP_200_OK)

class BookView(APIView):
    def get(self, request):
        book = BookModel.objects.all() #returns all details
        serializer = BookSerializer(book, many=True) #many true-> when ur trying to serialize many details
        return Response(serializer.data)
    
    def post(self, request): #request-> what user is sending to us and who is sending?
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid(): #checks if the data being send is correct as in not img in txt field
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class BookViewWithId(APIView):
    def get_object(self, id):
        try:
            book= BookModel.objects.get(pk=id)
            return book
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        book = self.get_object(id)
        serialzer = BookSerializer(book)
        return Response(serialzer.data)
    
    def put(self, request, id):
        book = self.get_object(id)
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        book = self.get_object(id)
        book.delete()
        return Response(status=status.HTTP_200_OK)
    
class UserBooksView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(UserModel, id=user_id)
        books = BookModel.objects.filter(user=user)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        user = get_object_or_404(UserModel, id=user_id)
        data = request.data.copy()
        data["user"] = user.id  # Assign the user ID to the book data

        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
