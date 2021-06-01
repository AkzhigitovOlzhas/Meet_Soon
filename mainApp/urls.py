from django.urls import path
from .views import RegConference
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_conference', views.admin_conference, name='admin'),
    path('<int:conference_id>/result/', views.result, name='result'),
    path('conference/<int:pk>/', RegConference.as_view(), name='reg_conference'),
    path('create_conference', views.create_conference, name='create_conference'),
    path('delete/<int:conference_id>/', views.delete, name='delete'),
    path('edit/<int:conference_id>/', views.edit, name='edit'),
    path('requests/<int:conference_id>/', views.requests, name='requests'),
]
