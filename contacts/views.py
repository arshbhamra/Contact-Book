from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Contacts 
from .forms import RegisterForm, LoginForm, ContactForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def home(request):
    return render(request, 'contacts/home.html')

def about(request):
    return render(request, 'contacts/about.html')

@login_required
def contacts(request):
   
#    contacts = Contacts.objects.all()
   contacts = Contacts.objects.filter(user=request.user)
   
   return render( request, 'contacts/contacts.html', {'contacts':contacts})



def greet(request, name, age):
    data = {
        'username' : name,
        'userage' : age
    }
    
    Contacts.objects.create(
           user=request.user,
           name="hei",
           city="kaad",
           phone="4567323",
           email="awddafc@ww.com"
       )
    
    return render(request, 'contacts/greeting.html', data)


@login_required
def add_contact(request):
    
    if request.method == 'POST':
       form = ContactForm(request.POST) 


       if form.is_valid():
           
          contact = form.save(commit=False)
          contact.user = request.user
          contact.save()
          return redirect("/app/contacts/") 

    else:
          form = ContactForm()
          
    return render(
                  request, 
                  "contacts/add_contact.html",
                  {"form": form}
                )         


@login_required
def edit_contact(request, pk):


    contact = get_object_or_404(Contacts, pk=pk,user=request.user)
    
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
        {
         "form": form, 
         "contact": contact
        }
    )
    
    
@require_POST
@login_required
def delete_contact(request, pk):
    
    contact = get_object_or_404(Contacts, pk=pk, user=request.user)
    contact.delete()
    return redirect("/app/contacts/")



def register(request):
    
    if request.method == "POST":
        
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
    
        
def user_login(request):
    
    if request.method == 'POST':
        
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            
            user = form.get_user()
            login(request, user)
            return redirect("/app/contacts/")
        
    else:
        form = LoginForm()
    
    return render(
        request,
        'contacts/login.html',
        {"form": form}
    )
    

@require_POST
def user_logout(request):

    logout(request)
    
    return redirect("login")

    
    
    
    
    
    
    
    
    
    