from django.urls import path
from blog import views
urlpatterns = [
    path('blog/', view=views.blogs, name='blog'),
    path('blog/detail/<int:pk>/', view=views.blog_detail, name='blog_detail'),
    path('blog/<category>/', view=views.blog_category, name='blog_category'),

]