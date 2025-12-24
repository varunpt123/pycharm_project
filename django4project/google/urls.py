from . import views
from django.urls import path

urlpatterns = [

    path('',views.first,name='first data'),
    path('products',views.second,name='second_data'),
    path('student',views.third,name='third_data')


]