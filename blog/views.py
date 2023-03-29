from django.shortcuts import render, redirect
from blog.models import Post, Comment, Category
from blog.forms import CommentForm
# Hamma Bloglar Ro'yxatini qaytaruvchi funksiya
def blogs(request):
    blogs = Post.objects.all().order_by('-created_on')
    categories = Category.objects.all()
    context = {
        'blogs': blogs,
        'total': len(blogs),
        'categories': categories,
    }
    return render(request, 'blog/blogs.html', context)

# Blogni #tag(category) bo'yicha filter qilib olish uchun
def blog_category(request, tag):
    # Tag (Kategoriya title)li bo'yicha Postlarni qidirib topish uchun
    posts = Post.objects.filter(category__title__contains=tag).order_by('-created_on')
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'tag': tag,
        'count': len(posts),
        'categories': categories,
    }
    return render(request, 'blog/category.html', context)



# Blog haqida batavsil ma'lumot beruvchi funksiya
def blog_detail(request, pk):
    # Hamma Kategoriyalarni bazadan olish uchun
    categories = Category.objects.all()
    comments = 0
    try:
        post = Post.objects.get(pk=pk)
        # Agar Post bo'lsa kommentariyani qidirush uchun
        if post:
            comments = Comment.objects.filter(post=post).order_by('-created_on')
        else:
            comments = None

    except:
        post = None
    
    # Kommentariya qoldirish
    # Foydalanuvchiga Kamment Formani ko'rsatish uchun
    form = CommentForm()
    # Komment Formadan kelgan ma'lumotlarni filter qilib ma'lumotlar bazasiga saqlash
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Komment Formaga yozilgan ma'lumotlarni olish uchun
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            # Ma'lumotlarni ma'lumotlar bazasiga saqlash uchun
            comment.save()
            # Formaga yozilgan ma'lumot refresh qilganda qayta-qayta bazaga saqlashni so'ramasligi uchun
            return redirect(f'/blog/detail/{post.id}')

    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'categories': categories,
        'count_comments': len(comments if comments else [])
    }
    return render(request, 'blog/detail.html', context)