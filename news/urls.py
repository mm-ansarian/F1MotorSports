from django.urls import path
from .views import *


urlpatterns = [
    path('list/', ListNewsView.as_view(), name='list_news_page'),
    path('mine/', MyNewsView.as_view(), name='my_news_page'),
    path('create/', CreateNewsView.as_view(), name='create_news_page'),
    path('retrieve/<int:pk>/', RetrieveNewsView.as_view(), name='retrieve_news_page'),
    path('update/<int:pk>/', UpdateNewsView.as_view(), name='update_news'),
    path('delete/<int:pk>/', DeleteNewsView.as_view(), name='delete_news'),
]
