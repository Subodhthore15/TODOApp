from django.contrib import admin
from django.urls import path
from todoapp.views import *
urlpatterns = [
    path('',alltodos,name="alltodos"),
    path('delete_item/<int:pk>/',deleteItem,name="deleteItem"),
    path('update_item/<int:pk>/',updateItem,name="updateItem"),
]
