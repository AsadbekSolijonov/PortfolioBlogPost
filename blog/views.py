from django.shortcuts import render, redirect
from blog.models import Post, Comment
from blog.forms import CommentForm
# Hamma Bloglar Ro'yxati qaytaruvchi funksiya
def blogs(request):
    blogs = Post.objects.all()
    reverse_blogs = blogs.order_by('-created_on')
    context = {
        'blogs': reverse_blogs
    }
    return render(request, 'blog/blogs.html', context)

# Blog category filter qilib qidirib olish.
def blog_category(request, category):
    posts = Post.objects.filter(category__title__contains=category).order_by('-created_on')
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'blog/category.html', context)



# Blog haqida batavsil ma'lumot beruvchi funksiya
def blog_detail(request, pk):
    try:
        blog_detail = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=blog_detail)
    except:
        blog_detail = None
        comments = None
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=blog_detail
            )
            comment.save()
            return redirect(f'/blog/detail/{blog_detail.id}')

    comment = Comment.objects.filter(post=blog_detail)
    context = {
        'blog_detail': blog_detail,
        'comments': comments.order_by('-created_on'),
        'form': form
    }
    return render(request, 'blog/detail.html', context)