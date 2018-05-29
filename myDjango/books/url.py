# urls.py
from django.urls import path
from books.views import PublisherList

urlpatterns = [
    path('', PublisherList.as_view()),
]