from django.contrib import admin
from .models import Post, Comment, PostView, Like, Category

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Like)
admin.site.register(Category)