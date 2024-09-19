from django.urls import path
from fibonacci import views

urlpatterns = [
    path('fibonacci/', views.fibonacci_view, name='fibonacci'),
]
