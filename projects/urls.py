from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='project_index'),
    path('projects/<int:pk>/', views.details, name='project_detail'),
    path('resume/', views.resume_view, name='resume'),
    path('pdf/', views.generate_resume_pdf, name='resume_pdf'),
]