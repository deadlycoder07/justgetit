from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path(r'form1/', views.form1, name='form1'),
	path(r'form2/', views.form2, name='form2'),
	path(r'form3/', views.form3, name='form3'),
	path(r'obgenerate/',views.orderform,name="ob"),
]
