from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Content, Tag, Branch

admin.site.register(Content)
admin.site.register(Tag)
admin.site.register(Branch)
