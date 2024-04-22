from django.urls import path
from .views import UserRegistration


urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-registration'),
    # path('signin/', views.signin, name='signin'),
]
