from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return f'blog/{instance.author.id}/{filename}'

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(
        upload_to=user_directory_path, default='no_image.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title
    
    def get_comment_count(self):
        return self.comment_set.count()
    
    def get_like_count(self):
        return self.like_set.count()
    
    def get_postview_count(self):
        return self.postview_set.count()
    
    def get_comments(self):
        return self.comment_set.all()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ('-time_stamp',)        


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
