from django.urls import path
from .views import *


urlpatterns = [
    path('details/', AccountDetailsView.as_view(), name='account_details_page'),
    path('signup/', SignupView.as_view(), name='signup_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
]
