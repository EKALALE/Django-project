
from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),#url mapping
    path('', views.about),#url mapping
    path('product/', views.product),#url mapping

]
