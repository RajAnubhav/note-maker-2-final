from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views # this will help the user to change the password

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name="change_password"),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name="change_password"),
]