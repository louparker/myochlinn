from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Post
from .forms import BlogForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage


def all_posts(request):
    """ This view shows all posts and also sorting and search queries """

    posts = Post.objects.all()
    p = Paginator(posts, 8)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    query = None
    categories = None

    page = posts

    context = {
        'posts': page,
        'on_blog_pages': True,  # to not show bag contents
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, post_id):
    """ This view shows specific post information """

    posts = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = posts
            comment.save()

            return redirect(reverse('post_detail', args=[posts.id]))
    else:
        form = CommentForm()

    context = {
        'post': posts,
        'form': form,
    }

    return render(request, 'blog/post_detail.html', context)


@login_required
def add_post(request):
    """ Add a post to the blog """
    if not request.user.is_superuser:
            messages.error(request, 'Sorry, only management can do that.')
            return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.info(request, 'Successfully added post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
        'on_blog_pages': True  # to not show bag contents
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """ Edit a post in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only management can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.info(request, 'Successfully updated post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Delete a post from the store """
    if not request.user.is_superuser:
            messages.error(request, 'Sorry, only management can do that.')
            return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.info(request, 'Post deleted!')
    return redirect(reverse('posts'))
