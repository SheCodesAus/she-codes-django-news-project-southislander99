from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('user-profile/<str:username>/', views.UserProfileView.as_view(), name='userProfile'),
    # path('user-profile/<int:pk>/', views.UserProfileView.as_view(), name='userProfile'),
]