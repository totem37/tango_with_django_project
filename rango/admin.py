from django.contrib import admin
from rango.models import Category, Page

# This class modifies Categories on the admin page for rango
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# This class modifies the appearance of the admin page for rango
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
