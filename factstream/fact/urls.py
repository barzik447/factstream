from django.urls import path
from . import views

urlpatterns = [
    path('fact/cat/', views.CatFact.as_view())
]
