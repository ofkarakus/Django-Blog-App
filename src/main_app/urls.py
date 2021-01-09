from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.display_home_page, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('post_list/', views.display_post_list, name='post_list'),
    path('post/<int:id>/details/', views.display_post_details, name='post_details'),
]
