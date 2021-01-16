from django.shortcuts import get_object_or_404, redirect, render
from main_app.forms import CommentForm, PostForm
from main_app.models import Post

# Create your views here.


def display_home_page(request):
    return render(request, 'main_app/home_page.html')


def create_post(request):
    form = PostForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('main:home')
    return render(request, 'main_app/create_post.html', context)


def display_post_list(request):
    post_list = Post.objects.filter(status='p')
    context = {
        'post_list': post_list
    }
    return render(request, 'main_app/post_list.html', context)


def display_post_details(request, slug):
    form = CommentForm()
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("main:post_details", slug=slug)
            # return redirect(request.path)
    context = {
        'post': post,
        'form': form
    }

    return render(request, 'main_app/post_details.html', context)


def update_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    context = {
        'form': form,
        'post': post
    }
    if form.is_valid():
        form.save()
        return redirect("main:post_list")

    return render(request, 'main_app/update_post.html', context)


def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    if request.method == 'POST':
        post.delete()
        return redirect('main:post_list')
    return render(request, 'main_app/delete_post.html', context)
