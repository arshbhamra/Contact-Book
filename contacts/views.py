from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Contacts 
from .forms import RegisterForm, LoginForm, ContactForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q


def home(request):
    return render(request, 'contacts/home.html')

def about(request):
    return render(request, 'contacts/about.html')

@login_required
def contact_detail(request, pk):

    contact = get_object_or_404(
        Contacts,
        pk=pk,
        user=request.user
    )

    recent_ids = request.session.get(
        "recent_contact_ids",
        []
    )

    # Remove duplicate ID
    if contact.pk in recent_ids:
        recent_ids.remove(contact.pk)

    # Add latest viewed contact first
    recent_ids.insert(0, contact.pk)

    # Keep only the latest five
    recent_ids = recent_ids[:5]

    # Save updated list in session
    request.session["recent_contact_ids"] = recent_ids

    return render(
        request,
        "contacts/contact_detail.html",
        {"contact": contact}
    )

@login_required
def recent_contacts(request):

    recent_ids = request.session.get(
        "recent_contact_ids",
        []
    )

    # Fetch only the current user's contacts
    contacts = Contacts.objects.filter(
        user=request.user,
        pk__in=recent_ids
    )

    # Preserve session order
    contacts_by_id = {
        contact.pk: contact
        for contact in contacts
    }

    ordered_contacts = [
        contacts_by_id[contact_id]
        for contact_id in recent_ids
        if contact_id in contacts_by_id
    ]

    return render(
        request,
        "contacts/recent_contacts.html",
        {"contacts": ordered_contacts}
    )



@login_required
def contacts(request):
   
#    contacts = Contacts.objects.all()
   contacts_list = Contacts.objects.filter(user=request.user).order_by("id")
   
   query = request.GET.get("q", "")
   city_query = request.GET.get("city", "")

   if city_query:
        contacts_list = contacts_list.filter(
            city__iexact = city_query
        )
   
   if query:
       contacts_list = contacts_list.filter(
           Q(name__icontains=query) |
           Q(email__icontains=query) |
           Q(city__icontains=query) |
           Q(phone__icontains=query)
       )
   
   
   paginator = Paginator(contacts_list,7)
   
   page_num = request.GET.get("page")

   page_obj = paginator.get_page(page_num)
   
   return render( 
            request, 
            'contacts/contacts.html',
            {
                "page_obj": page_obj,
                "query": query, 
                "city": city_query,
            }
        )


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

       Contacts.objects.create(
          user=request.user,
          name = "arsh",
          city = "khanna",
          phone = "45632",
          email = "arsh@arsh.com"
        )
    
       if form.is_valid():

             contact = form.save(commit=False)
             contact.user = request.user
             contact.save()
             messages.success(request, "Contact saved successfully")
             return redirect("/app/contacts/") 

       else:
             messages.error(request, "Contact not Saved !!")

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
            messages.success(request, "Contact update successfully !")
            return redirect("/app/contacts/")
        
    else:
        form = ContactForm(instance=contact)
        messages.error(request, "Contact couldnt not update.")
    
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
    messages.success(request, "Contact deleted Success !!!")
    
    return redirect("/app/contacts/")


def register(request):
    
    if request.method == "POST":
        
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration Success !!!")
            
            return redirect("login")
        
    else:
        form = RegisterForm()
        messages.error(request, "Registration Failed !!!")
        
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
            messages.success(request, "Login Success !!!")
            return redirect("/app/contacts/")
        
    else:
        form = LoginForm()
        messages.error(request, "Login Failed !!!")
    
    return render(
        request,
        'contacts/login.html',
        {"form": form}
    )
    

@require_POST
def user_logout(request):

    logout(request)
    messages.success(request, "Logout Successfull !")
    
    return redirect("login")

    
    
    
    
    
    
    
    
    
    