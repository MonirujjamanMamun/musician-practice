from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_album, name='add_album'),
    path('edit/<int:id>', views.album_edit, name='add_edit'),
    path('delete/<int:id>', views.album_delete, name='add_delete'),
]
