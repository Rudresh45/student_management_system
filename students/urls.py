from django.urls import path
from . import views
app_name = 'students'
urlpatterns = [
path('', views.dashboard, name='dashboard'),
path('list/', views.student_list, name='student_list'),
path('create/', views.student_create, name='student_create'),
path('edit/<int:pk>/', views.student_edit, name='student_edit'),
path('delete/<int:pk>/', views.student_delete, name='student_delete'),
]
