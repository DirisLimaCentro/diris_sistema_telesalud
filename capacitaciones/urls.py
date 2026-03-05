from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('nuevo/', views.video_create, name='video_create'),
    path('detalle/<int:pk>/', views.video_detail, name='video_detail'),
    path('video/<int:pk>/editar/', views.video_update, name='video_update'),
    path('video/<int:pk>/delete/', views.video_delete, name='video_delete'),
]