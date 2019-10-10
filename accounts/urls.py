from django.urls import path
from django.views import SignUpView
# from django.views import login, signup

app_name= 'accounts'

urlpatterns = [
    
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
