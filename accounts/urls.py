from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile/profile_change/', views.ProfileChangeView.as_view(), name='profile_change'),
    path('profile/profile_success/', views.profile_success, name='profile_success'),
    path('profile/password_change/', views.PasswordChangeViewe.as_view(), name='password_change'),
    path('profile/password_success/', views.password_success, name='password_success'),
    path('profile/image_change/', views.profile, name='image_change'),
    path('profile/profile_image_success/', views.image_success, name='image_changed'),
]
