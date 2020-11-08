from django.urls import path
from . import views

app_name = 'phonenumber'

urlpatterns = [
    path('',views.home , name='home'),
    path('Create/', views.Forms , name='create'),
    path('addnumber/<int:data>/', views.AddNumberform , name='AddNumber'),
    path('update/<int:pk>/',views.updateForms, name='update'),
    path('delete/<int:pk>/',views.delete , name='delete'),
]