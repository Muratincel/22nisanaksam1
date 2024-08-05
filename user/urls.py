from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister, name="register"),
    path('login/', userLogin, name="login"),
    path('logout/', userLogout, name="logout"),
    path('profiles/', profiles, name="profiles"),
    path('create/', createProfil, name="create"),
    path('delete/<int:profile_id>', delete_profile, name="delete"),
    path('edit/<int:profile_id>', edit_profile, name="edit"),
    path('hesap/', hesap, name="hesap"),
    path('password_change/', passwordChange, name="password_change"  ),
    path('account_delete/', account_delete, name="account_delete"  ),
]