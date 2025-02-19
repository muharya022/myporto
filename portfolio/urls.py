from django.urls import path
from . import views  
from django.contrib.auth.views import LoginView
from .views import CustomLoginView

urlpatterns = [
    path('', views.about_me, name='about_me'),
    path('contact/', views.contact_view, name='contact'),
    path('messages/', views.messages_list, name='messages_list'),
    path('messages/read/<int:message_id>/', views.mark_as_read, name='mark_as_read'),
    path('messages/<int:message_id>/delete/', views.delete_message, name='delete_message'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('edit-project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('add_project/', views.add_project, name='add_project'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
]