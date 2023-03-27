from django.shortcuts import render, redirect
from blog.models import Post, Comment, Category
from blog.forms import CommentForm
# Hamma Bloglar Ro'yxati qaytaruvchi funksiya
def blogs(request):
    blogs = Post.objects.all()
    reverse_blogs = blogs.order_by('-created_on')
    all_categories = Category.objects.all()
    context = {
        'blogs': reverse_blogs,
        'total': len(reverse_blogs),
        'all_categories': all_categories,
    }
    return render(request, 'blog/blogs.html', context)

# Blog category filter qilib qidirib olish.
def blog_category(request, category):
    posts = Post.objects.filter(category__title__contains=category).order_by('-created_on')
    all_categories = Category.objects.all()
    context = {
        'posts': posts,
        'category': category,
        'total': len(posts),
        'all_categories': all_categories,
    }
    return render(request, 'blog/category.html', context)



# Blog haqida batavsil ma'lumot beruvchi funksiya
def blog_detail(request, pk):
    comments = 0
    try:
        blog_detail = Post.objects.get(pk=pk)
        if blog_detail:
            comments = Comment.objects.filter(post=blog_detail).order_by('-created_on')
        else:
            comments = None
    except:
        blog_detail = None
        
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

    context = {
        'blog_detail': blog_detail,
        'comments': comments,
        'form': form,
        'count_comments': len(comments if comments else [])
    }
    return render(request, 'blog/detail.html', context)