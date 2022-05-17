from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='homepage'),
    path('upload/',views.upload,name='uploadpage'),
    path('delete/<int:book_id>',views.delete),
    path('update/<int:book_id>',views.update),
]
