from django.urls import path
from . import views

urlpatterns = [
    path('gold/', views.root),
    path('process',views.show)
]
