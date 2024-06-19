from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('compose/', views.compose_view, name='compose'),
    path('inbox/', views.inbox_view, name='inbox'),
    path('generate_email/', views.generate_email_view, name='generate_email'),
]
