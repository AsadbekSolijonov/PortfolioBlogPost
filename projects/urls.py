from django.urls import path
from projects import views

urlpatterns = [
    path('projects/', views.project, name='project'),
    path('all_projects/', views.all_projects, name='all_projects'),
    path('all_projects/<int:pk>/', views.project_detail, name='project_detail'),
]
