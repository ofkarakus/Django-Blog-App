from django.shortcuts import redirect, render
from main_app.forms import PostForm
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
    post_list = Post.objects.all()
    context = {
        'post_list': post_list
    }
    return render(request, 'main_app/post_list.html', context)
