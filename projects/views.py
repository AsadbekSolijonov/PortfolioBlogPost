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
        detail = Project.objects.get(pk=pk)
    except:
        detail = None
    context = {
        'detail': detail,
    }
    return render(request, 'projects/project_detail.html', context)
