from django.shortcuts import render
from projects.models import Project

# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/project_index.html', context)


def project_details(request, pk):
    projects = Project.objects.get(pk=pk)
    context = {'project': projects}
    return render(request, 'projects/project_detail.html', context)