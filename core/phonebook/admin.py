from django.contrib import admin
from .models import *

# Register your models here.

class NumberPhoneInline(admin.TabularInline):
    '''Tabular Inline View for NumberPhone'''

    model = NumberPhone
    min_num = 1
    max_num = 3
    extra = 0
    # raw_id_fields = (,)


@admin.register(NumberPhone)
class NumberPhoneAdmin(admin.ModelAdmin):
    '''Admin View for NumberPhone'''

    list_display = ('PhoneNumber','contact')
    list_filter = ('PhoneNumber','contact')
    search_fields = ('PhoneNumber','contact')



@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('first_name', 'last_name')
    inlines = [
        NumberPhoneInline,
    ]
    search_fields = ('first_name', 'last_name')





