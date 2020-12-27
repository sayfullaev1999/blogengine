from django.urls import path, include
from .views import SignUp

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup_url'),  # Вход на сайт
]
