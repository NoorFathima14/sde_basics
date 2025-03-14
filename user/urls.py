from django.urls import path
from .views import UserView, UserViewWithIds,BookView, BookViewWithId, UserBooksView

urlpatterns = [
    # Book URLs
    path("books/", BookView.as_view(), name="book-list"),  
    path("books/<int:id>/", BookViewWithId.as_view(), name="book-details"),

    # User URLs
    path("users/", UserView.as_view(), name="user-list"),  
    path("users/<int:id>/", UserViewWithIds.as_view(), name="user-details"),

    path('users/<int:user_id>/books/', UserBooksView.as_view(), name='user-books'),
]