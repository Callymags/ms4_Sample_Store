from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages

from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def blog(request):
    """ View for displaying blog posts and adding new blog posts """
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)


def post(request, slug):
    """ View for displaying and editing individual blog posts """
    post = Post.objects.get(slug=slug)

    context = {
        'post': post,
        'form': form,
        'on_blog_post_page': True,

    }
    return render(request, 'blog/post.html', context)


@login_required
def add_post(request):
    """ Add a blog post to the blog page """
    slugs = list(Post.objects.all().values_list('slug', flat=True))

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to \
            add a blog post.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = str(request.user)
            post.slug = slugify(post.title)
            if post.slug in slugs:
                messages.error(request, 'A blog post with that title \
                    already exists.')
            else:
                post.save()
                form.save_m2m()
                messages.success(request, f'Blog post "{post.title}" \
                                successfully added!')
                return redirect('blog')
        else:
            messages.error(request, 'Failed to add blog post. \
                        Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
        'on_blog_page': True,
    }

    return render(request, template, context)