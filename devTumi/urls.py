from django.urls import path
from . import views

app_name='devTumi'

urlpatterns = [
    path('',views.index,name='index')
]