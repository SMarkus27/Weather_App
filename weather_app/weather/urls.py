from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_city),
    path('delete/<city>',views.delete_city),

]
