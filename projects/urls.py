from django.urls import path
from projects import views
from django.urls import include 


urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:pk>/', views.project_details, name='project_detail'),
    path('pages', include('pages.urls')),
    

]