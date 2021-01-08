from django import forms
from .models import Category, Post, Comment


class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.OPTIONS)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="Select")

    class Meta:
        model = Post
        exclude = ('slug', 'author', 'last_update', 'publish_date')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )
