from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .form import ProjectForm
from .models import DaftarProject
from django.contrib.auth import authenticate

# Create your views here.

# @login_required(login_url='login')
# class MainProjects():
def index(request):

    return render(request, 'index.html')

def project_list(request):

    datas = DaftarProject.objects.all()
    return render(request, 'projects/project_list.html', {'datas':datas})

def project_new(request):
    if request.method == 'POST':
        
        form = ProjectForm(request.POST)
        # print(form)
        
        if form.is_valid:
            post = form.save(commit=False)
            post.username = request.user
            post.save()

            return HttpResponseRedirect(reverse('projects:list'))
        
    else:
        form = ProjectForm()
    return render(request, 'projects/project_edit.html', {'form':form})

def project_edit(request, pk):
    master = get_object_or_404(DaftarProject, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=master)
        if form.is_valid():
            master = form.save(commit=False)
            master.save()
            return redirect('projects:detail', pk=master.pk)
    else:
        form = ProjectForm(instance=master)
        return render(request, 'projects/project_edit.html', {'form':form})

def project_detail(request, pk):
    datas = get_object_or_404(DaftarProject, pk=pk)

    return render(request, 'projects/project_detail.html', {'datas':datas})

    
