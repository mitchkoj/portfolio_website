from django.shortcuts import render
from .models import Project


def project_index(request):
    """
        An index view that shows a snippet of information
        about each project.
    """

    # get all project objects in the database
    projects = Project.objects.all()

    # dictionary argument for render engine
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    """
        An detail view that shows more information
        on a particular topic.

        takes a project id.
    """

    # get the project with primary key 
    project = Project.objects.get(pk=pk)

    # dictionary argument for render engine
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
