from django.urls import path
from .views import SignUpView #,ChangePassword

urlpatterns = [
    path('signup/',SignUpView.as_view(), name='signup'),
    # path('passwd/',ChangePassword.as_view(), name='changepasswd'),
]