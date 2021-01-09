from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.display_home_page, name='home'),
    path('create_post/', views.create_post, name='create_post')
]