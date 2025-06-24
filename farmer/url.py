from django.urls import path
from api.views import UserLoginView, UserProfileView, UserRegisterView, APIHomeView  # Ensure APIHomeView is imported
from rest_framework.authtoken.views import obtain_auth_token
from .views import LoginView, UserDetailView, ResetPasswordView, DeleteUserView, EditUserView

app_name = 'api'
urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/user/', UserDetailView.as_view(), name='user-detail'),
    path('api/reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('api/user/delete/', DeleteUserView.as_view(), name='delete-user'),
    path('api/user/edit/', EditUserView.as_view(), name='edit-user'),
]
