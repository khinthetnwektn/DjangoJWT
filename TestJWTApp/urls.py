from django.urls import path
from . import views

urlpatterns = [
    # path('hello/', views.hello, name='hello'),
    path('hello/', views.HelloView.as_view(), name='hello'),
]