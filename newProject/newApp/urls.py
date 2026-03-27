
from django.urls import path
from . import views


urlpatterns = [
    path('',views.app_index, name='app_index'),
    path('new/', views.new_view, name='new_view'),

]