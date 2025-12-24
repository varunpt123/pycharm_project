from django.urls import path

from . import views

urlpatterns = [
    path('',views.first,name='firstdata'),
    path('add',views.second,name='threads'),
    path('hai',views.third,name='third'),
    path('hallo',views.fourth,name='fourth'),
    path('tview',views.teacher_form,name='fourth_data'),
    path('hview',views.form2,name='fifth_data'),
    path('cview/<int:id>',views.form3,name='sixth_data')



]