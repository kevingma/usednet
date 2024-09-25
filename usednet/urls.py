from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('content/<int:pk>/', views.content_detail, name='content_detail'),
    path('branch/<int:pk>/', views.branch_detail, name='branch_detail'),
    path('add_branch/content/<int:content_pk>/', views.add_branch, name='add_branch_content'),
    path('add_branch/branch/<int:parent_pk>/', views.add_branch, name='add_branch_branch'),
    path('tag/<str:tag_name>/', views.tag_view, name='tag_view'),
]
