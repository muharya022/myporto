from django.shortcuts import render
from .models import Project

def about_me(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

# portfolio/views.py

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

from django.shortcuts import render, redirect
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Redirect ke halaman daftar proyek setelah ditambahkan
    else:
        form = ProjectForm()
    return render(request, 'portfolio/add_project.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectDeleteForm

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')  # Ganti dengan URL yang sesuai
    
    return render(request, 'portfolio/delete_project.html', {'project': project})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def logout_view(request):
    logout(request)
    messages.success(request, 'Berhasil logout!')
    return redirect('about_me')

from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.is_read = False  # Pesan baru dianggap belum dibaca
            contact_message.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def messages_list(request):
    messages_list = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'portfolio/messages_list.html', {'messages_list': messages_list})

def mark_as_read(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    message.is_read = True
    message.save()
    return redirect('messages_list')

def delete_message(request, message_id):
    message_obj = get_object_or_404(ContactMessage, id=message_id)
    message_obj.delete()
    messages.success(request, "Pesan berhasil dihapus.")
    return redirect('messages_list')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Project
from .forms import ProjectForm

def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proyek berhasil diperbarui!')
            return redirect('project_list')
        else:
            print(form.errors)  # Cek terminal untuk error
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/edit_project.html', {'form': form, 'project': project})
