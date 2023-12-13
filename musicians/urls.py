from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_musicians, name='add_musicians'),
    path('edit/<int:id>', views.edit_musicians, name='edit_musicians'),
]
