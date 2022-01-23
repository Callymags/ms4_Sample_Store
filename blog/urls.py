from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add/', views.add_post, name='add_post'),
    path('<slug:slug>/', views.post, name='post'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post,
         name='delete_post'),
]