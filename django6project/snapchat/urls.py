from django.urls import path

from . import views

from snapchat import views

urlpatterns = [
    path('',views.first,name='firstdata'),
    path('product',views.second,name='second_data'),
    path('hallo',views.third,name='third_data'),
    path('tview',views.teacher_form,name='fourth_data'),
    path('tread',views.form2,name='fifth_data'),
    path('cview/<int:id>',views.form3,name='sixth_data'),
    path('dview/<int:id>',views.form4,name='seventh_data')


]