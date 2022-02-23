from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('user-profile/<str:username>/', views.UserProfileView.as_view(), name='userProfile'),
    path('edit-profile/<str:username>/', views.EditProfileView.as_view(), name='editProfile'),
    # path('user-profile/<int:pk>/', views.UserProfileView.as_view(), name='userProfile'),
]