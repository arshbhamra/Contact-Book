from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Contacts 
from .forms import RegisterForm

def home(request):
    return render(request, 'contacts/home.html')

def about(request):
    return render(request, 'contacts/about.html')

def contacts(request):
   
   contacts = Contacts.objects.all()
   
   return render( request, 'contacts/contacts.html', {'contacts':contacts})

def greet(request, name, age):
    data = {
        'username' : name,
        'userage' : age
    }
    return render(request, 'contacts/greeting.html', data)

def add_contact(request):
    
    if request.method == 'POST':
       form = ContactForm(request.POST) 

       if form.is_valid():
          form.save()
          return redirect("/app/contacts/") 

    else:
          form = ContactForm()
          
    return render(
                  request, 
                  "contacts/add_contact.html",
                  {"form": form}
                )         

def edit_contact(request, pk):


    contact = get_object_or_404(Contacts, pk=pk)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            return redirect("/app/contacts/")
        
    else:
        form = ContactForm(instance=contact)
    
    return render(
        request,
        "contacts/edit_contact.html",
        {"form": form, "contact": contact}
    )

def register(request):
    
    if request.method == "POST" :
        
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
        
    else:
        form = RegisterForm()
        
    return render(
        request,
        "contacts/register.html",
        {"form": form}
    )
        