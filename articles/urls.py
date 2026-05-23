from django.urls import path
from .views import *


urlpatterns = [
    path('list/', ListArticlesView.as_view(), name='list_articles_page'),
    path('create/', CreateArticleView.as_view(), name='create_article_page'),
    path('retrieve/<int:pk>', RetrieveArticleView.as_view(), name='retrieve_article_page'),
    path('update/<int:pk>', UpdateArticleView.as_view(), name='update_article_page'),
    path('delete/<int:pk>', DeleteArticleView.as_view(), name='delete_article_page'),
]
