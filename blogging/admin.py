from django.contrib import admin
from .models import Blog, ContactForm

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']

@admin.register(ContactForm)
class AdminContact(admin.ModelAdmin):
    list_display = ['id','email', 'Phone'] 