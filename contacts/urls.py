from django.urls import path
from contacts import views

urlpatterns = [

    path('home/', views.home, name="home"),
    path('contacts/', views.contacts, name="contacts"),
    path('about/', views.about, name="about"),
    path('greet/<str:name>/<int:age>/', views.greet, name="greet"),
    path('add-contact/', views.add_contact, name="add_contact"),
    path('edit-contact/<int:pk>/', views.edit_contact, name="edit_contact"),
    path('delete-contact/<int:pk>/', views.delete_contact, name="delete_contact"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('recent/', views.recent_contacts, name="recent_contacts"),
    path('contact/<int:pk>/', views.contact_detail, name="contact_detail"),

]