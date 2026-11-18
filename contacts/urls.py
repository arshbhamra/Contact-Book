from django.urls import path
from contacts import views

urlpatterns = [

    path('home/', views.home, name="home"),
    path('contacts/', views.contacts, name="contacts"),
    path('about/', views.about, name="about"),
    path('greet/<str:name>/<int:age>/', views.greet, name="greet"),
    path('add-contact/', views.add_contact, name="add_contact"),
    path('edit-contact/<int:pk>/', views.edit_contact, name="edit_contact"),
    path('register/', views.register, name="register"),

]