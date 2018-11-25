from django.urls import path, re_path

from . import views

urlpatterns = [
    # example: /tasks/
    path('', views.index, name='index'),
    # example: /tasks/5/
    path('<int:task_id>/', views.details, name='details'),
    # example: /tasks/create/
    path('create/', views.create, name='create'),
    # example: /tasks/create/
    path('<int:task_id>/edit/', views.edit, name='edit'),
    # example: /tasks/5/save/
    path('<int:task_id>/save/', views.save, name='save'),
    # example: /tasks/delete/
    path('<int:task_id>/delete/', views.delete, name='delete'),
    # example: /tasks/search/
    re_path(r'^search/$', views.search, name='search')

]