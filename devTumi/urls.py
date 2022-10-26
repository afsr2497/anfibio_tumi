from django.urls import path
from . import views

app_name='devTumi'

urlpatterns = [
    path('',views.index,name='index'),
    path('gamepadButton',views.gamepadButton,name='gamepadButton'),
    path('gamepadFront',views.gamepadFront,name='gamepadFront'),
    path('mainView',views.mainView,name='mainView'),
]