from django import forms
from .models import *


class ContactsForm(forms.ModelForm):
   # Metadata
    class Meta:
        model = Contacts
        exclude = ['picture','description']
        fields = ['first_name','last_name']
        error_messages ={
            'first_name':{
                'required': "این فیلد اجباری است",
            },
            'last_name':{
                'required': "این فیلد اجباری است",
            }
        }
        labels = {
            'first_name' : 'نام :',
            'last_name' : 'نام خانوادگی :'
        }
        widgets = {
            'first_name' : forms.TextInput(
                attrs = {'placeholder': 'نام',
                        'class': 'form-control',
                }),
            'last_name' : forms.TextInput(
                attrs = {
                    'placeholder': 'نام خانوادگی',
                    'class': 'form-control',
                }
            )
        }


class PhoneNumberForm(forms.ModelForm):

    class Meta:
        model = NumberPhone
        fields =['PhoneNumber','contact']
        widgets ={
            'contact' : forms.HiddenInput(),
        }


