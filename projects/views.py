from django.shortcuts import render
from projects.models import Project
# Create your views here.
def project(request):
    return render(request, 'projects/projects.html')


def all_projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects,
    }
    return render(request, 'projects/projects.html', context)


def project_detail(request, pk):
    try: 
        project_detail = Project.objects.get(pk=pk)
    except:
        project_detail = None
    context = {
    'detail': project_detail, 
    }
    return render(request, 'projects/project_detail.html', context)