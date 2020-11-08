from django.db import models

class Contacts(models.Model):
    picture = models.ImageField(default='image_default/default.jpg',upload_to='images/', verbose_name='تصویر',blank=True, null=True)
    first_name = models.CharField(max_length=200, verbose_name='نام', blank=False , null=False)
    last_name = models.CharField(max_length=200,verbose_name='نام خانوادگی', blank=False , null=False)
    description = models.TextField(max_length=500,blank=True, null=True, verbose_name='توضیحات')
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def get_number(self):
        return self.contact_number.all()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'نام'
        verbose_name_plural = 'اسامی'

class NumberPhone(models.Model):
    PhoneNumber = models.CharField(max_length=12,blank=False, null=False,verbose_name='شماره تلفن')
    contact = models.ForeignKey(to=Contacts, on_delete=models.CASCADE ,blank=True, null=True , related_name='contact_number',verbose_name='مخاطبان')
    def __str__(self):
        return f'this {self.PhoneNumber}'

    class Meta:
        verbose_name = 'شماره'
        verbose_name_plural ='شماره ها'

