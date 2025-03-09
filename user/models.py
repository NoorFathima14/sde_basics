from django.db import models

# Create your models here.

#user schema
class UserModel(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username
    
class BookModel(models.Model):
    bookname = models.CharField(max_length=30)
    author =models.CharField(max_length=30)
    published_date=models.DateField()
    #isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.bookname