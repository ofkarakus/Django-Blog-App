from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.display_home_page, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('post_list/', views.display_post_list, name='post_list'),
    path('post/<str:slug>/details/', views.display_post_details, name='post_details'),
    path('post/<str:slug>/delete/', views.delete_post, name='delete_post'),
    path('post/<str:slug>/update/', views.update_post, name='update_post'),
    path('post/<str:slug>/like/', views.like_post, name='like_post'),
]
