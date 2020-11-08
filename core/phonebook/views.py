from django.shortcuts import render , HttpResponse , get_object_or_404 ,redirect
from .models import Contacts
from django.forms import formset_factory
from .forms import *

# Create your views here.

def home(request):
    search = request.GET.get('name')
    if search != None:
        search = search.split(' ')[0]
        first = Contacts.objects.filter(first_name__icontains=search)
        last = Contacts.objects.filter(last_name__icontains=search)
        if first:
            contacts = first
        elif last:
            contacts = last
        else:
            contacts = None
    else:
        contacts = Contacts.objects.all()
    context = {
        'contacts':contacts
    }
    return render(request , 'work/index.html',context)


def Forms(request):
    form = ContactsForm(request.POST or None)
    if form.is_valid():
        contact = form.save()
        return redirect('phonenumber:AddNumber',contact.id)
    context = {
        'form':form,
    }
    return render(request,'forms/form.html',context)

def AddNumberform(request,data):
    contact = get_object_or_404(Contacts , id =data)
    form = PhoneNumberForm(request.POST or None,initial={'contact':contact})
    if form.is_valid():
        form.save()
        return redirect('phonenumber:home')
    context = {
        'form':form
    }
    return render(request,'forms/form.html',context)

def updateForms(request,pk):
    contacts = get_object_or_404(Contacts,id=pk)
    form = ContactsForm(request.POST or None,instance=contacts)
    if form.is_valid():
        contact = form.save()
        return redirect('phonenumber:home')
    context = {
        'form':form,
    }
    return render(request,'forms/form.html',context)

def delete(request,pk):
    contact = get_object_or_404(Contacts, id=pk )
    contact.delete()
    return redirect('phonenumber:home')
