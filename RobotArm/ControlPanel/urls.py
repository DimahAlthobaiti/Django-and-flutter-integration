from django.urls import path
from . import views

urlpatterns = [
    path('', views.control_panel, name='control_panel'),      
    path('run/', views.run_values_view, name='run_display'), 
]