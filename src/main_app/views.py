from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main_app.forms import CommentForm, PostForm
from main_app.models import Post, Like
from django.contrib.auth.decorators import login_required

# Create your views here.


def display_home_page(request):
    return render(request, 'main_app/home_page.html')

@login_required()
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

    # def commenton_thepost()
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

@login_required()
def update_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    context = {
        'form': form,
        'post': post
    }
    if request.user.id != post.author.id:
        return redirect("main:post_list")
        # return HttpResponse("You're not authorized!")
    if form.is_valid():
        form.save()
        return redirect('main:post_details', slug=slug)

    return render(request, 'main_app/update_post.html', context)

@login_required()
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    if request.user.id != post.author.id:
        return redirect("main:post_list")
        # return HttpResponse("You're not authorized!")
    if request.method == 'POST':
        post.delete()
        return redirect('main:post_list')
    return render(request, 'main_app/delete_post.html', context)

@login_required()
def like_post(request, slug):
    if request.method == "POST":
        post = get_object_or_404(Post, slug=slug)
        like = Like.objects.filter(post=post, user=request.user)
        if like.exists():
            like.delete()
        else:
            Like.objects.create(user=request.user, post=post)
        return redirect('main:post_details', slug=slug)
